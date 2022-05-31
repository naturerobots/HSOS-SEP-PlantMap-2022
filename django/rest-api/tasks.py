import sys

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import grpc
import point_cloud_service_pb2_grpc as PointCloudService
from celery import Celery
from geometry_query_pb2 import GeometryQuery
from google.protobuf.json_format import MessageToDict

app = Celery('tasks', backend='rpc://', broker='amqp://rabbitmq')

SERVER_URL = "seerep.naturerobots.de:5000"
channel = grpc.insecure_channel(SERVER_URL)


@app.task
def dl_pcloud(geometries, puuid):
    pointCloudStub = PointCloudService.PointCloudServiceStub(channel)
    success = []
    failed = []
    for index, geometry in enumerate(geometries):

        geometryQuery = GeometryQuery(projectuuid=puuid, geometryuuid=geometry['uuid'])

        try:
            response = pointCloudStub.GetPointCloud2ByUUID(geometryQuery)
            dictionary = MessageToDict(response)
            # success.append({"geometry": str(geometry), "responseDict": str(dictionary)})
            success.append({"geometry": str(geometry)})
            print("SUCCESS: " + str(index) + " " + str(geometry))
        # except:
        except Exception as e:
            # e = sys.exc_info()[0]
            failed.append({"geometry": str(geometry), "error": str(e)})
            print("FAILED: " + str(index) + " " + str(geometry))
    response = {
        "stats": {
            "total": len(success) + len(failed),
            "success": len(success),
            "failed": len(failed),
        },
        "success": success,
        "failed": failed,
    }
    return response
