import base64
import logging
import os
import re
import string
import sys
from uuid import uuid4

import grpc

# generated grpc python files
sys.path.append(r'../build/gRPC/')

import label_service_pb2_grpc as labelService
import measurement_service_pb2_grpc as measurementService
import meta_operations_service_pb2_grpc as metaOperations
from class_query_pb2 import ClassQuery
from geometry_query_pb2 import GeometryQuery
from google.protobuf.json_format import MessageToDict
from knox.views import LoginView as KnoxLoginView
from project_query_pb2 import ProjectQuery
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import login
from django.http import *

from . import tasks
from .models import *

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
# https://github.com/tensorflow/serving/issues/1382
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]
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


# /user-info
@api_view(['GET'])
def getUser(request):

    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data, safe=False)


# /companies
@api_view(['GET'])
def getCompanies(request):

    # TODO Check if authenticated user is allowed to request company_id, garden_id

    try:
        companies = Company.objects.filter(user=request.user)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}
@api_view(['GET'])
def getCompany(request, company_id: int):

    # TODO Check if authenticated user is allowed to request company_id, garden_id

    try:
        company = Company.objects.get(id=company_id, user=request.user)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    serializer = CompanySerializer(company)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens
@api_view(['GET'])
def getGardens(request, company_id: int):

    # TODO Check if authenticated user is allowed to request company_id, garden_id

    try:
        company = Company.objects.get(id=company_id, user=request.user)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    gardens = Garden.objects.filter(company=company)
    serializer = GardenSerializer(gardens, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens/{garden_id}
@api_view(['GET'])
def getGarden(request, company_id: int, garden_id: int):

    # TODO Check if authenticated user is allowed to request company_id, garden_id

    try:
        company = Company.objects.get(id=company_id, user=request.user)
    except:
        # Company with id company_id not found in database or does not belong to the user requesting it
        return HttpResponseNotFound()

    try:
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        # Garden with id garden_id not found in database or does not belong to the company
        return HttpResponseNotFound()

    serializer = GardenSerializer(garden)
    return JsonResponse(serializer.data, safe=False)


# TODO add authentication
@api_view(['POST'])
def uploadGardenImage(request, garden_id):
    if not request.data['image']:
        return HttpResponseBadRequest('Missing Image in request')

    if not request.data['positions']:
        return HttpResponseBadRequest('Missing Positions in request')

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

    # create image model
    try:
        garden = Garden.objects.get(pk=garden_id)
    except Garden.DoesNotExist:
        return HttpResponseBadRequest(f"Garden number {garden_id} does not exists")
    garden.image_path = filename
    garden.save()

    # save coordinates
    for position in request.data['positions']:
        try:
            Coordinate(image=garden, **position).save()
        except TypeError:
            return HttpResponseBadRequest("Wrong format of the positions in requests")

    return HttpResponse(status=201)


# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: int, garden_id: int):

    # TODO Check if authenticated user is allowed to request company_id, garden_id

    try:
        company = Company.objects.get(id=company_id, user=request.user)
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

    # TODO Check if authenticated user is allowed to request company_id, garden_id, bed_id

    try:
        company = Company.objects.get(id=company_id, user=request.user)
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
