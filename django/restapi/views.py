import json
import string
import sys

from . import tasks
from .forms import *

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import logging

import grpc
import label_service_pb2_grpc as labelService
import measurement_service_pb2_grpc as measurementService
import meta_operations_service_pb2_grpc as metaOperations
from class_query_pb2 import ClassQuery
from geometry_query_pb2 import GeometryQuery
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from knox.views import LoginView as KnoxLoginView
from measurement_pb2 import Measurement
from project_query_pb2 import ProjectQuery
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import *
from django.template import loader

from .models import *

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)
stubLabel = labelService.LabelServiceStub(channel)
stubMeasurement = measurementService.MeasurementServiceStub(channel)

# /login
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


# /register
class RegisterView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            authserializer = AuthTokenSerializer(data=request.data)
            if authserializer.is_valid():
                user = authserializer.validated_data['user']
                login(request, user)
                return super(RegisterView, self).post(request, format=None)
            return Response(authserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Authorization methods

# Checks if given user-id is valid
def isUserIdValid(user_id):
    if not user_id or not isinstance(user_id, int) or user_id < 1:
        return False
    return True


# Checks if given permission is valid
def isPermissionValid(permission):
    if not permission or not permission in ['u', 'a']:
        return False
    return True


# Checks if given permission is user permission
def isUser(permission):
    if not permission or not permission in 'u':
        return False
    return True


# Checks if given permission is admin permission
def isAdmin(permission):
    if not permission or not permission in 'a':
        return False
    return True


# Checks if a HTTP request contains necessary keys and valid values
# to create a new permission in corresponding endpoints
def isCreatePermissionRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'user_id' in data or not 'permission' in data:
        return False

    if not isPermissionValid(data['permission']) or not isUserIdValid(data['user_id']):
        return False

    # Deny overwriting users own permissions
    if request.user.id == data['user_id']:
        return False

    return True


# Checks if a HTTP request contains necessary keys and valid values
# to remove a new permission in corresponding endpoints
def isRemovePermissionRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'user_id' in data:
        return False

    if not isUserIdValid(data['user_id']):
        return False

    # Deny removing users own permissions
    if request.user.id == data['user_id']:
        return False

    return True


# Checks if a HTTP request contains necessary keys and valid values
# to create a new company or garden in corresponding endpoints
def isCreateCompanyOrGardenRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'name' in data:
        return False

    if not data['name']:
        return False

    return True


# Returns True, if user_id is allowed to access company_id
def isCompanyUser(company_id, user_id):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(id=user_id)
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        serializer = CompanyPermissionSerializer(companyPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    permission = serializer.data['permission']
    if not isUser(permission) and not isAdmin(permission):
        return False

    return True


# Returns True, if user_id is admin of company_id
def isCompanyAdmin(company_id, user_id):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(id=user_id)
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        serializer = CompanyPermissionSerializer(companyPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    if not isAdmin(serializer.data['permission']):
        return False

    return True


# Function to create a new company permission
# Returns True, if permission was created successfully
def createCompanyPermission(company_id, user_id, permission):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(id=user_id)

        # Filter for permission, update if exists or create new permission
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        if companyPermission:
            companyPermission.permission = permission
            companyPermission.save()
        else:
            CompanyPermission.objects.create(permission=permission, company=company, user=user)

        return True
    except:
        return False


# Endpoint to give a user permissions for a company
@api_view(['POST'])
def createCompanyPermissionView(request, company_id: int):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isCreatePermissionRequestValid(request):
        return HttpResponseBadRequest()

    inputData = json.loads(request.body)

    if not createCompanyPermission(company_id, inputData['user_id'], inputData['permission']):
        return HttpResponseBadRequest()

    return HttpResponse(status=201)


# Function to remove a users permissions for a company
# Returns True, if permission was deleted successfully or does not exist
def removeCompanyPermission(company_id, user_id):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(id=user_id)

        # Filter for permission and delete it
        CompanyPermission.objects.filter(company=company, user=user).delete()

        return True
    except:
        return False


# Endpoint to remove a users permissions for a company
@api_view(['POST'])
def removeCompanyPermissionView(request, company_id: int):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isRemovePermissionRequestValid(request):
        return HttpResponseBadRequest()

    if not removeCompanyPermission(company_id, json.loads(request.body)['user_id']):
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


# Returns True, if user_id is allowed to access garden_id
def isGardenUser(garden_id, user_id):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(id=user_id)
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        serializer = GardenPermissionSerializer(gardenPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    permission = serializer.data['permission']
    if not isUser(permission) and not isAdmin(permission):
        return False

    return True


# Returns True, if user_id is admin of garden_id
def isGardenAdmin(garden_id, user_id):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(id=user_id)
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        serializer = GardenPermissionSerializer(gardenPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    if not isAdmin(serializer.data['permission']):
        return False

    return True


# Function to create a new garden permission
# Returns True, if permission was created successfully
def createGardenPermission(garden_id, user_id, permission):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(id=user_id)

        # Filter for permission, update if it already exists or create a new permission
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        if gardenPermission:
            gardenPermission.permission = permission
            gardenPermission.save()
        else:
            GardenPermission.objects.create(permission=permission, garden=garden, user=user)

        return True
    except:
        return False


# Endpoint to give a user permissions for a garden
@api_view(['POST'])
def createGardenPermissionView(request, company_id: int, garden_id: int):

    # Check if requesting user has admin permissions on garden or company
    if not isGardenAdmin(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isCreatePermissionRequestValid(request):
        return HttpResponseBadRequest()

    inputData = json.loads(request.body)

    if not createGardenPermission(garden_id, inputData['user_id'], inputData['permission']):
        return HttpResponseBadRequest()

    return HttpResponse(status=201)


# Function to remove a garden permission
# Returns True, if permission was deleted successfully or does not exist
def removeGardenPermission(garden_id, user_id):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(id=user_id)

        # Filter for permission and delete it
        GardenPermission.objects.filter(garden=garden, user=user).delete()

        return True
    except:
        return False


# Endpoint to remove a users permissions for a garden
@api_view(['POST'])
def removeGardenPermissionView(request, company_id: int, garden_id: int):

    # Check if requesting user has admin permissions on garden or company
    if not isGardenAdmin(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isRemovePermissionRequestValid(request):
        return HttpResponseForbidden()

    if not removeGardenPermission(garden_id, json.loads(request.body)['user_id']):
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


# End of authorization methods


# /user
@api_view(['GET'])
def getUser(request):

    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data, safe=False)


# Endpoint that returns all companies a user has permissions on
def getCompanies(request):

    try:
        companyPermissions = CompanyPermission.objects.filter(user=request.user)
    except:
        return HttpResponseBadRequest()

    companies = []
    for p in companyPermissions.iterator():
        companies.append(p.company)

    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to create a new company
def createCompany(request):

    if not isCreateCompanyOrGardenRequestValid(request):
        return HttpResponseBadRequest()

    try:
        company = Company.objects.create(name=json.loads(request.body)['name'])
    except:
        return HttpResponseBadRequest()

    # Give the user admin permissions on new company
    # Delete company if permission could not be set successfully
    if not createCompanyPermission(company.id, request.user.id, 'a'):
        Company.objects.delete(company)
        return HttpResponseBadRequest()

    return JsonResponse({'id': company.id})


# /companies
@api_view(['GET', 'POST'])
def companies(request):

    # GET: Endpoint that returns all companies a user has permissions on
    if request.method == 'GET':
        return getCompanies(request)

    # POST: Endpoint to create a new company
    elif request.method == 'POST':
        return createCompany(request)


# /companies/{company_id}
@api_view(['GET'])
def getCompany(request, company_id: int):

    # Check if requesting user is allowed to access company
    if not isCompanyUser(company_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponseBadRequest()


# Endpoint that returns all gardens of the requested company the user has permissions on
def getGardens(request, company_id):

    # Check if requesting user is allowed to access company
    userIsCompanyAdmin = isCompanyAdmin(company_id, request.user.id)
    if not isCompanyUser(company_id, request.user.id) and not userIsCompanyAdmin:
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        gardens = Garden.objects.filter(company=company)
    except:
        return HttpResponseBadRequest()

    # Company admin can access all gardens
    if userIsCompanyAdmin:
        serializer = GardenSerializer(gardens, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Check company user permissions on each garden
    authorizedGardens = []
    for g in gardens.iterator():
        if GardenPermission.objects.filter(user=request.user, garden=g).count() > 0:
            authorizedGardens.append(g)

    serializer = GardenSerializer(authorizedGardens, many=True)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to create a new garden
def createGarden(request, company_id):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isCreateCompanyOrGardenRequestValid(request):
        return HttpResponseBadRequest()

    # Create new garden
    try:
        company = Company.objects.get(id=company_id)
        garden = Garden.objects.create(name=json.loads(request.body)['name'], company=company, image=None)
    except:
        return HttpResponseBadRequest()

    return JsonResponse({'id': garden.id})


# /companies/{company_id}/gardens
@api_view(['GET', 'POST'])
def gardens(request, company_id: int):

    # GET: Endpoint that returns all gardens of the requested company the user has permissions on
    if request.method == 'GET':
        return getGardens(request, company_id)

    # POST: Endpoint to create a new garden
    elif request.method == 'POST':
        return createGarden(request, company_id)


# /companies/{company_id}/gardens/{garden_id}
@api_view(['GET'])
def getGarden(request, company_id: int, garden_id: int):

    # Check if requesting user is allowed to access the garden
    if not isGardenUser(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        return HttpResponseBadRequest()

    serializer = GardenSerializer(garden)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens/{garden_id}/image
@api_view(['GET', 'POST'])
def gardenImage(request, company_id: int, garden_id: int):

    # Check if authenticated user is allowed to request company_id, garden_id
    if isGardenUser(garden_id, request.user.id) == False:
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    try:
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        # Garden with id garden_id not found in database or does not belong to the company
        return HttpResponseNotFound()

    if request.method == 'GET':
        return HttpResponseRedirect(garden.image.url)

    # Example request with curl:
    # curl --form image='@/home/user/image.png' http://localhost:8000/companies/1/gardens/1/image
    #  -H "Authorization: Token 7182c8ddc808ac13d6befd1791816aabb66a6048048861720603c431b9589d7c"
    elif request.method == 'POST':

        if isGardenAdmin(garden_id, request.user.id) == False:
            return HttpResponseForbidden()

        gardenForm = GardenForm(request.POST, request.FILES)

        if gardenForm.is_valid():

            # Delete previous garden image if it exists
            if garden.image:
                garden.image.delete(save=True)

            garden.image = gardenForm.cleaned_data['image']
            garden.save()
            return JsonResponse({"success": "true"})

    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: int, garden_id: int):

    # Check if authenticated user is allowed to request company_id, garden_id
    if isGardenUser(garden_id, request.user.id) == False:
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    try:
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        # Garden with id garden_id not found in database or does not belong to the company
        return HttpResponseNotFound()

    # Get all beds of the garden
    beds = Bed.objects.filter(garden=garden)

    # Get bed data from SEEREP over gRPC
    bedsData = []
    for bed in beds:
        try:
            bedData = stub.GetProjectDetails(ProjectQuery(projectuuid=bed.uuid))
            bedsData.append(MessageToDict(bedData))
        except:
            return JsonResponse({})

    return JsonResponse(bedsData, safe=False)


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/crops
@api_view(['GET'])
def getCrops(request, company_id: int, garden_id: int, bed_id: int):

    # Check if authenticated user is allowed to request company_id, garden_id, bed_id
    if isGardenUser(garden_id, request.user.id) == False:
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    try:
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        # Garden with id garden_id not found in database or does not belong to the company
        return HttpResponseNotFound()

    try:
        bed = Bed.objects.get(id=bed_id, garden=garden)
    except:
        # Bed with id bed_id not found in database or does not belong to the garden
        return HttpResponseNotFound()

    # Get bed data from SEEREP over gRPC

    try:
        bedData = stub.GetProjectDetails(ProjectQuery(projectuuid=bed.uuid))
    except:
        return JsonResponse({})

    bedDataDict = MessageToDict(bedData)

    # Seperate pointcloud and measurement geometries:
    # - Every crop has one pointcloud geometry and one measurement geometry
    # - cropsPointclouds(1) and cropsMeasurements(1) refer to the same crop

    cropsPointclouds = []
    cropsMeasurements = []

    for crop in bedDataDict['geometries']:

        if crop['type'] == "pointcloud":
            cropsPointclouds.append(crop)

        elif crop['type'] == "measurement":
            cropsMeasurements.append(crop)

    # Get instances and classes of cropsPointclouds from SEEREP over gRPC

    # instances = []
    classes = []

    classUUIDsRequested = []

    for crop in cropsPointclouds:
        # instanceLabel = crop['labels'][0]
        classLabel = crop['labels'][1]

        # Skip gRPC request if class was already requested once
        if classUUIDsRequested.__contains__(bed.uuid):
            classes.append(classes[len(classes) - 1])
            continue

        try:
            classData = stubLabel.GetClass(ClassQuery(projectuuid=bed.uuid, classuuid=classLabel))
            classUUIDsRequested.append(bed.uuid)
        except:
            return JsonResponse({})

        classes.append(MessageToDict(classData))

    # Get measurements of cropsMeasurements from SEEREP over gRPC

    measurements = []

    for crop in cropsMeasurements:

        try:
            measurementData = stubMeasurement.GetMeasurementByUUID(
                GeometryQuery(projectuuid=bed.uuid, geometryuuid=crop['uuid'])
            )
        except:
            return JsonResponse({})

        measurements.append(MessageToDict(measurementData))

    # Collect and put together all needed data over a single crop

    crops = []

    for i in range(len(cropsPointclouds) - 1):

        plantName = cropsPointclouds[i]['name']
        variety = "N/A"
        location = bed_id
        soilHumidity = 0
        health = "N/A"
        healthLoglevel = 0
        status = "N/A"
        harvest = 0
        approxYield = 0

        try:
            variety = classes[i]['attributes']['variety']['stringData']
        except:
            pass

        try:
            # Expects geometry "ground" to be at the last position in "measurements" and that every
            # crop in the current bed is planted on "ground"
            soilHumidity = measurements[len(measurements) - 1]['data']['humidity']['doubleData']
        except:
            pass

        try:
            health = measurements[i]['data']['warn_msg']['stringData']
            healthLoglevel = int(measurements[i]['data']['warn_level']['int64Data'])
            status = measurements[i]['data']['status']['stringData']
            harvest = measurements[i]['data']['growth_state']['doubleData']
            approxYield = int(measurements[i]['data']['approx_yield']['int64Data'])
        except:
            pass

        crops.append(
            {
                'plant': plantName,
                'variety': variety,
                'location': location,
                'soil_humidity': soilHumidity,
                'health': health,
                'health_loglevel': healthLoglevel,
                'status': status,
                'harvest': harvest,
                'yield': approxYield,
            }
        )

    return JsonResponse(crops, safe=False)


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/sensors
@api_view(['GET'])
def getSensors(request, company_id: int, garden_id: int, bed_id: int):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/sensors/{sensor_id}
@api_view(['GET'])
def getSensor(request, company_id: int, garden_id: int, bed_id: int, sensor_id: int):
    return JsonResponse({})


# companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/3d
@api_view(['GET'])
def getBed3DImage(request, company_id: int, garden_id: int, bed_id: int):
    return JsonResponse({})


@api_view(['POST'])
def make_task(request, uuid: string) -> Response:
    if request.method == 'POST':
        logger.info("views.py make_task POST")
        response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
        geometries = MessageToDict(response)['geometries']
        tasks.dl_pcloud.delay(geometries, uuid)
        return Response(status=202)
