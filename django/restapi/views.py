import json
import string
import sys

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import logging

import grpc
import meta_operations_service_pb2_grpc as metaOperations
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from project_query_pb2 import ProjectQuery
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import ObjectDoesNotExist
from django.http import *
from django.template import loader

from .models import Bed, Company, Garden, User

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)


@api_view(['GET'])
def list_projects(request) -> Response:
    if request.method == 'GET':
        response = stub.GetProjects(empty_pb2.Empty())
        return Response(MessageToDict(response))


@api_view(['GET'])
def list_project_detials(request, uuid: string) -> Response:
    if request.method == 'GET':
        response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
        return Response(MessageToDict(response))


# /login
@api_view(['GET'])
def login(request):
    return JsonResponse({})


# /register
@api_view(['POST'])
def register(request):
    return JsonResponse({})


# /users/{user-id}
@api_view(['GET'])
def getUsers(request, user_id: string):
    return JsonResponse({})


# /companies/{company_id}
@api_view(['GET'])
def getCompanies(request, company_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens
@api_view(['GET'])
def getGardens(request, company_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}
@api_view(['GET'])
def getGardenInfo(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/image
@api_view(['GET', 'POST'])
def gardenImage(request, company_id: string, garden_id: string):
    if request.method == 'GET':
        template = loader.get_template('restapi/image.html')
        context = {}
        return HttpResponse(template.render(context, request))

    elif request == 'POST':
        return JsonResponse({})

    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/plants
@api_view(['GET'])
def getPlants(request, company_id: string, garden_id: string):
    # Dummy-data!
    return JsonResponse(
        {
            'plants': [
                {
                    'name': 'Mangold',  # Plant name
                    'variety': 'Mangold',  # Plant variety
                    'location': 1,  # Bed/Row number
                    'soil_humidity': 65,  # Soil humidity for plant area in %
                    'health': 'N/A',  # Health statuses: 'N/A', 'Disease Detection', 'Nutrient Deficiency', 'Watering', 'Good'
                    'health_loglevel': 1,  # Importance of health status: 1 (Info), 2 (Attention), 3 (Warning)
                    'status': 'Sprout',  # Plant growth statuses: 'Sprout', 'Seedling', 'Vegetating', 'Budding', 'Flowering', 'Ripening'
                    'harvest': 150,  # Time until harvesting in days (0 = harvest today)
                    'yield': 100,  # 0 = N/A
                },
                {
                    'name': 'Beans',
                    'variety': 'Beans',
                    'location': 1,
                    'soil_humidity': 65,
                    'health': 'Good',
                    'health_loglevel': 1,  # Importance of health status: 1 (Info), 2 (Attention), 3 (Warning)
                    'status': 'Seedling',
                    'harvest': 120,
                    'yield': 243,
                },
                {
                    'name': 'Chicory',
                    'variety': 'Chicory',
                    'location': 1,
                    'soil_humidity': 65,
                    'health': 'Watering',
                    'health_loglevel': 2,
                    'status': 'Vegetating',
                    'harvest': 90,
                    'yield': 222,
                },
                {
                    'name': 'Courgette',
                    'variety': 'Courgette',
                    'location': 1,
                    'soil_humidity': 65,
                    'health': 'Nutrient Deficiency',
                    'health_loglevel': 2,
                    'status': 'Budding',
                    'harvest': 60,
                    'yield': 540,
                },
                {
                    'name': 'Pumpkin',
                    'variety': 'Pumpkin',
                    'location': 1,
                    'soil_humidity': 65,
                    'health': 'Disease Detection',
                    'health_loglevel': 3,
                    'status': 'Flowering',
                    'harvest': 30,
                    'yield': 140,
                },
                {
                    'name': 'Spinach',
                    'variety': 'Spinach',
                    'location': 1,
                    'soil_humidity': 65,
                    'health': 'Good',
                    'health_loglevel': 1,
                    'status': 'Ripening',
                    'harvest': 10,
                    'yield': 200,
                },
            ]
        }
    )


# /companies/{company_id}/gardens/{garden_id}/plant/{plant_id}
@api_view(['GET'])
def getBeds(request, company_id: string, garden_id: string, plant_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}
@api_view(['GET'])
def getBedInfo(request, company_id: string, garden_id: string, bed_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/3D
@api_view(['GET'])
def getBed3dImage(request, company_id: string, garden_id: string, bed_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/sensors
@api_view(['GET'])
def getSensors(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/sensors/{sensor_id}
@api_view(['GET'])
def getSensorInfo(request, company_id: string, garden_id: string, sensor_id: string):
    return JsonResponse({})


@api_view(['POST'])
def make_task(request, uuid: string) -> Response:
    if request.method == 'POST':
        logger.info("views.py make_task POST")
        response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
        geometries = MessageToDict(response)['geometries']
        tasks.dl_pcloud.delay(geometries, uuid)
        return Response(status=202)
