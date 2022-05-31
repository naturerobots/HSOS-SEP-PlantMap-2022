import string
import sys

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import grpc
import meta_operations_service_pb2_grpc as metaOperations
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from project_query_pb2 import ProjectQuery
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

from .models import Company, Garden, User

SERVER_URL = "seerep.naturerobots.de:5000"
channel = grpc.insecure_channel(SERVER_URL)

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
@api_view(['GET'])
def register(request):
    return JsonResponse({})


# /users/{user-id}
@api_view(['GET'])
def getUsers(request, user_id: string):
    return JsonResponse({})


# /companies/{company-id}
@api_view(['GET'])
def getCompanies(request, company_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens
@api_view(['GET'])
def getGardens(request, company_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}
@api_view(['GET'])
def getGardenInfo(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/image
@api_view(['GET'])
@api_view(['POST'])
def gardenImage(request, company_id: string, garden_id: string):
    if request.method == 'GET':
        return JsonResponse({})
    elif request.method == 'POST':
        return JsonResponse({})
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/beds
@api_view(['GET'])
def getBeds(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/beds/{beds-id}
@api_view(['GET'])
def getBedInfo(request, company_id: string, garden_id: string, bed_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/beds/{beds-id}/3D
@api_view(['GET'])
def getBed3dImage(request, company_id: string, garden_id: string, bed_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/sensors
@api_view(['GET'])
def getSensors(request, company_id: string, garden_id: string):
    return JsonResponse({})


# /companies/{company-id}/gardens/{gardenId}/sensors/{sensor-id}
@api_view(['GET'])
def getSensorInfo(request, company_id: string, garden_id: string):
    return JsonResponse({})
