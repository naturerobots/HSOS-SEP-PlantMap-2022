import base64
import json
import logging
import os
import re
import string
import sys
from time import time

import grpc

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import label_service_pb2_grpc as labelService
import measurement_service_pb2_grpc as measurementService
import meta_operations_service_pb2_grpc as metaOperations
import numpy as np
import tf_service_pb2_grpc as tfService
from class_query_pb2 import ClassQuery
from conversions.transform_coordinates import llOfPlant
from geometry_query_pb2 import GeometryQuery
from google.protobuf.json_format import MessageToDict
from header_pb2 import Header
from instance_query_pb2 import InstanceQuery
from knox.views import LoginView as KnoxLoginView
from project_query_pb2 import ProjectQuery
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import Coordinate, Garden
from transform_stamped_query_pb2 import TransformStampedQuery

from django.contrib.auth import login
from django.http import *
from django.urls import reverse

from . import tasks
from .models import *

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)
stubLabel = labelService.LabelServiceStub(channel)
stubMeasurement = measurementService.MeasurementServiceStub(channel)
stubTf = tfService.TfServiceStub(channel)

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
        garden = Garden.objects.create(name=json.loads(request.body)['name'], company=company, image_path=None)
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


def uploadImage(request, company_id, garden_id):

    if not 'coordinates' in request.data or not 'image' in request.data:
        return HttpResponseBadRequest()

    # Check if requesting user has admin permissions on garden
    if not isGardenAdmin(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    # split image string to get file extension and raw bytes
    imageInfo, imageData = request.data['image'].split(',')
    infos = re.split(':|/|;', imageInfo)

    # TODO add env variable for storage location
    path = "/workdir/django/storage/images"
    if not os.path.exists(path):
        os.mkdir(path)

    # create unique file name
    if infos[2] != 'png':
        return HttpResponseBadRequest('We currently only support PNGs')
    filename = f"{path}/{uuid4()}.png"

    # decode bytes
    try:
        with open(filename, 'wb') as image:
            image.write(base64.b64decode(imageData))
    except FileNotFoundError:
        return HttpResponseBadRequest("Wrong format of image string in request")

    try:
        garden = Garden.objects.get(pk=garden_id)
    except Garden.DoesNotExist:
        return HttpResponseBadRequest(f"Garden number {garden_id} does not exists")
    garden.image_path = filename
    garden.save()

    for position in request.data['coordinates']:
        # if coordinates already exist just update, else create new ones
        try:
            coordinate = Coordinate.objects.get(name=position['name'])
            coordinate.latitude = position['latitude']
            coordinate.longitude = position['longitude']
            coordinate.save()
        except Coordinate.DoesNotExist:
            try:
                Coordinate(garden=garden, **position).save()
            except TypeError:
                return HttpResponseBadRequest("Wrong format of the positions in requests")

    return HttpResponse(status=201)


def getImage(request, company_id, garden_id):

    # Check if requesting user is allowed to access the garden
    if not isGardenUser(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    try:
        garden = Garden.objects.get(pk=garden_id)
    except Garden.DoesNotExist:
        return HttpResponseNotFound()

    if garden.image_path is None:
        return HttpResponseNotFound('No image uploaded for this garden')

    with open(garden.image_path, 'rb') as image:
        image_string = 'data:image/png;base64,' + base64.b64encode(image.read()).decode('ASCII')

    coordinates = garden.garden_coordinates.all()

    coordinates = CoordinateSerializer(coordinates, many=True).data

    return JsonResponse({"image": image_string, "coordinates": coordinates})


# TODO consider using class based views, for improved separation
@api_view(['GET', 'POST'])
def imageView(request, company_id: int, garden_id: int):
    if request.method == 'POST':
        return uploadImage(request, company_id, garden_id)
    elif request.method == 'GET':
        return getImage(request, company_id, garden_id)


# With the current dummy data this costs 100 gRPC-requests per bed. Seems like quite the DOS potential
# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: int, garden_id: int):

    # Check if requesting user is allowed to access the garden
    if not isGardenUser(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    requests = 0

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

    def streamGen(beds):

        # Get bed data from SEEREP over gRPC
        for bed in beds:

            try:
                bedData = stub.GetProjectDetails(ProjectQuery(projectuuid=bed.uuid))
            except:
                continue

            plys_missing = False

            tf_cache = {}

            plant_type = {}
            variety = {}
            soil_humidty = []
            harvest = []
            pyield = []
            health = {}
            plant_coords = []

            for plant in bedData.geometries:
                if plant.type == "pointcloud":
                    try:
                        if not (plant.frame_id in tf_cache):
                            tfresponse = stubTf.GetTransformStamped(
                                TransformStampedQuery(
                                    header=Header(seq=99, frame_id="map", uuid_project=bed.uuid),
                                    child_frame_id=plant.frame_id,
                                )
                            )
                            tf_cache[plant.frame_id] = tfresponse.transform

                        translation = tf_cache[plant.frame_id].translation
                        rotation = tf_cache[plant.frame_id].rotation

                        pcoords = llOfPlant(
                            bed.uuid,
                            plant.uuid,
                            bedData.geolocation.latitude,
                            bedData.geolocation.longitude,
                            np.array([translation.x, translation.y, translation.z]),
                            np.array([rotation.x, rotation.y, rotation.z, rotation.w]),
                        )

                        if pcoords is not None:
                            (lat, lon, h) = pcoords
                            plant_coords.append({"lat": lat, "lon": lon})
                        else:
                            plys_missing = True

                    except Exception as err:
                        pass

                if plant.type != "measurement":
                    continue

                # Maybe extract this into a function
                try:
                    measurement = stubMeasurement.GetMeasurementByUUID(
                        GeometryQuery(projectuuid=bed.uuid, geometryuuid=plant.uuid)
                    )
                    if "humidity" in measurement.data:
                        soil_humidty.append(measurement.data["humidity"].double_data)

                    if "approx_yield" in measurement.data:
                        pyield.append(measurement.data["approx_yield"].double_data)

                    for i in range(3):
                        if all(key in measurement.data for key in (f"health_{i}_type", f"health_{i}_level")):
                            htype = measurement.data[f"health_{i}_type"].string_data
                            hlevel = measurement.data[f"health_{i}_level"].int64_data
                            if htype in health:
                                health[htype].append(hlevel)
                            else:
                                health[htype] = [hlevel]

                    instance = stubLabel.GetInstance(InstanceQuery(projectuuid=bed.uuid, instanceuuid=plant.labels[0]))

                    if instance.name in plant_type:
                        plant_type[instance.name] += 1
                    else:
                        plant_type[instance.name] = 1

                    if "planting_date" in instance.attributes and "growth_state" in measurement.data:
                        planting_date: int = instance.attributes["planting_date"].int64_data
                        growth_state: float = measurement.data["growth_state"].double_data

                        harvest.append((time() - planting_date) * (1.0 - growth_state))

                except:
                    pass

                try:
                    pclass = stubLabel.GetClass(ClassQuery(projectuuid=bed.uuid, classuuid=plant.labels[1]))

                    if "variety" in pclass.attributes:
                        v = pclass.attributes["variety"].string_data
                        if v in variety:
                            variety[v] += 1
                        else:
                            variety[v] = 1

                except:
                    pass

            # Compute averages
            plant_type = max(plant_type, key=plant_type.get)
            variety = max(variety, key=variety.get)
            soil_humidty = float(sum(soil_humidty)) / float(len(soil_humidty))
            harvest = int((float(sum(harvest)) / float(len(harvest))) / 604800)
            pyield = float(sum(pyield)) / float(len(pyield))
            phealth = []
            for hkey, hval in health.items():
                phealth.append({"type": hkey, "loglevel": int((float(sum(hval)) / float(len(hval))))})
            plants_url = reverse(
                'plants-resource', kwargs={'company_id': company_id, 'garden_id': garden_id, 'bed_id': bed.id}
            )

            data = json.dumps(
                {
                    "id": bed.id,
                    "plant": plant_type,
                    "variety": variety,
                    "plants": request.build_absolute_uri(plants_url),
                    "soil_humidty": soil_humidty,
                    "harvest": f"{harvest} week",
                    "yield": pyield,
                    "health": phealth,
                    "plant_coords": plant_coords,
                }
            )

            if plys_missing:
                tasks.dl_pcloud.delay(MessageToDict(bedData)['geometries'], bed.uuid)

            yield data

    # logger.info(f"gRPC Requests: {requests}")
    # return JsonResponse({"beds": bedsData})
    return StreamingHttpResponse(streamGen(beds), content_type='application/json')


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/crops
@api_view(['GET'])
def getPlants(request, company_id: int, garden_id: int, bed_id: int):

    # Check if requesting user is allowed to access the garden
    if not isGardenUser(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    requests = 0

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
        return HttpResponseNotFound()

    plys_missing = False

    tf_cache = {}
    plant_coords = {}
    plantData = {}

    for plant in bedData.geometries:
        if plant.type == "pointcloud":
            try:
                if not (plant.frame_id in tf_cache):
                    tfresponse = stubTf.GetTransformStamped(
                        TransformStampedQuery(
                            header=Header(seq=99, frame_id="map", uuid_project=bed.uuid),
                            child_frame_id=plant.frame_id,
                        )
                    )
                    tf_cache[plant.frame_id] = tfresponse.transform

                translation = tf_cache[plant.frame_id].translation
                rotation = tf_cache[plant.frame_id].rotation

                pcoords = llOfPlant(
                    bed.uuid,
                    plant.uuid,
                    bedData.geolocation.latitude,
                    bedData.geolocation.longitude,
                    np.array([translation.x, translation.y, translation.z]),
                    np.array([rotation.x, rotation.y, rotation.z, rotation.w]),
                )

                if pcoords is not None:
                    (lat, lon, h) = pcoords
                    plant_coords[plant.name] = {"lat": lat, "lon": lon}
                else:
                    plys_missing = True

            except Exception as err:
                pass
        if plant.type != "measurement":
            continue

        plant_type = "Error"
        variety = "N/A"
        soil_humidty = 0.0
        harvest = 0
        pyield = 0.0
        health = []

        # Maybe extract this into a function
        try:
            requests += 1
            measurement = stubMeasurement.GetMeasurementByUUID(
                GeometryQuery(projectuuid=bed.uuid, geometryuuid=plant.uuid)
            )
            if "humidity" in measurement.data:
                soil_humidty = measurement.data["humidity"].double_data

            if "approx_yield" in measurement.data:
                pyield = measurement.data["approx_yield"].double_data

            for i in range(3):
                if all(key in measurement.data for key in (f"health_{i}_type", f"health_{i}_level")):
                    htype = measurement.data[f"health_{i}_type"].string_data
                    hlevel = measurement.data[f"health_{i}_level"].int64_data
                    health.append({"type": htype, "loglevel": hlevel})

            requests += 1
            instance = stubLabel.GetInstance(InstanceQuery(projectuuid=bed.uuid, instanceuuid=plant.labels[0]))

            plant_type = instance.name

            if "planting_date" in instance.attributes and "growth_state" in measurement.data:
                planting_date: int = instance.attributes["planting_date"].int64_data
                growth_state: float = measurement.data["growth_state"].double_data

                harvest = int(((time() - planting_date) * (1.0 - growth_state)) / 604800.0)

        except:
            pass

        try:
            requests += 1
            pclass = stubLabel.GetClass(ClassQuery(projectuuid=bed.uuid, classuuid=plant.labels[1]))

            if "variety" in pclass.attributes:
                variety = pclass.attributes["variety"].string_data

        except:
            pass

        plantData[plant.name] = {
            "id": plant.uuid,
            "bedid": bed.id,
            "plant": plant_type,
            "variety": variety,
            "soil_humidty": soil_humidty,
            "harvest": f"{harvest} week",
            "yield": pyield,
            "health": health,
        }

    newPlantData = []

    # This is stupid, don't tell me if it breaks
    for (name, plant) in plantData.items():
        if name in plant_coords:
            plant["plant_coords"] = plant_coords[name]
        newPlantData.append(plant)

    if plys_missing:
        tasks.dl_pcloud.delay(MessageToDict(bedData)['geometries'], bed.uuid)

    logger.info(f"gRPC Requests: {requests}")
    return JsonResponse({"plants": newPlantData})


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
