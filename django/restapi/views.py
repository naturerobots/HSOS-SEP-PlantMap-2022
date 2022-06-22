import json
import string
import sys

from . import tasks

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

from .models import *

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)


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
def getUser(request, user_id: int):
    return JsonResponse({})


# /companies/{company_id}
@api_view(['GET'])
def getCompany(request, company_id: int):
    company = Company.objects.filter(id=company_id)
    serializer = CompanySerializer(company, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens
@api_view(['GET'])
def getGardens(request, company_id: int):
    garden = Garden.objects.filter(company=company_id)
    serializer = GardenSerializer(garden, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens/{garden_id}
@api_view(['GET'])
def getGarden(request, company_id: int, garden_id: int):
    garden = Garden.objects.filter(id=garden_id, company=company_id)
    serializer = GardenSerializer(garden, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}/gardens/{garden_id}/image
@api_view(['GET', 'POST'])
def gardenImage(request, company_id: int, garden_id: int):
    if request.method == 'GET':
        template = loader.get_template('restapi/image.html')
        context = {}
        return HttpResponse(template.render(context, request))

    elif request == 'POST':
        return JsonResponse({})

    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: int, garden_id: int):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/sensors
@api_view(['GET'])
def getSensors(request, company_id: int, garden_id: int, bed_id: int):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/sensors/{sensor_id}
@api_view(['GET'])
def getSensor(request, company_id: int, garden_id: int, bed_id: int, sensor_id: int):
    return JsonResponse({})


# /companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/plants
@api_view(['GET'])
def getPlants(request, company_id: int, garden_id: int, bed_id: int):
    # garden = Garden.objects.filter(id=garden_id, company=company_id)
    # if not garden:
    #     return JsonResponse({})
    # beds = Bed.objects.filter(garden=garden[0].id)
    # serializer = BedSerializer(beds, many=True)

    # response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
    # return Response(MessageToDict(response))

    # Dummy-data!
    return JsonResponse(
        {
            'plants': [
                {
                    'plant': 'Mangold',  # Plant name
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
                    'plant': 'Beans',
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
                    'plant': 'Chicory',
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
                    'plant': 'Courgette',
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
                    'plant': 'Pumpkin',
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
                    'plant': 'Spinach',
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


# companies/{company_id}/gardens/{garden_id}/beds/{bed_id}/plants/{plant_id}/3d
@api_view(['GET'])
def getPlant3DImage(request, company_id: int, garden_id: int, bed_id: int, plant_id: int):
    return JsonResponse({})


@api_view(['POST'])
def make_task(request, uuid: string) -> Response:
    if request.method == 'POST':
        logger.info("views.py make_task POST")
        response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
        geometries = MessageToDict(response)['geometries']
        tasks.dl_pcloud.delay(geometries, uuid)
        return Response(status=202)
