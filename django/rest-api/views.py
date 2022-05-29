import string
import sys

from . import tasks

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import grpc
import meta_operations_service_pb2_grpc as metaOperations
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from project_query_pb2 import ProjectQuery
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def make_task(request) -> Response:
    if request.method == 'POST':
        result = tasks.add.delay(4, 4)
        return Response(result.get(timeout=1))
