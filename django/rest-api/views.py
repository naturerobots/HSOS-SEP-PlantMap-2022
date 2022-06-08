import string
import sys

from . import tasks

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import logging

import grpc
import meta_operations_service_pb2_grpc as metaOperations
import point_cloud_service_pb2_grpc as PointCloudService
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from project_query_pb2 import ProjectQuery
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def make_task(request, uuid: string) -> Response:
    if request.method == 'POST':
        logger.info("views.py make_task POST")
        response = stub.GetProjectDetails(ProjectQuery(projectuuid=uuid))
        geometries = MessageToDict(response)['geometries']
        tasks.dl_pcloud.delay(geometries, uuid)
        return Response(status=202)
