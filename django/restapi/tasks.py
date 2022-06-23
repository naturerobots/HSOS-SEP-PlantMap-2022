import sys
from pathlib import Path
from tokenize import String

# there is definitly a better way to add an import path
sys.path.append(r'../build/gRPC/')

import logging

import grpc
import point_cloud_service_pb2_grpc as PointCloudService
from celery import Celery
from geometry_query_pb2 import GeometryQuery
from google.protobuf.json_format import MessageToDict
from point_cloud_2_pb2 import PointCloud2

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage, default_storage

# from django.conf import settings
# settings.configure()

logger = logging.getLogger('django')

# Start Celery worker from 'django' directory with "celery -A rest-api.tasks worker --loglevel=info"
app = Celery('tasks')
app.config_from_object('celeryconfig')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)


@app.task
def dl_pcloud(geometries, puuid):
    pointCloudStub = PointCloudService.PointCloudServiceStub(channel)
    success = []
    failed = []
    for index, geometry in enumerate(geometries):

        geometryQuery = GeometryQuery(projectuuid=puuid, geometryuuid=geometry['uuid'])

        try:
            response: PointCloud2 = pointCloudStub.GetPointCloud2ByUUID(geometryQuery)
            # dictionary = MessageToDict(response)
            save_ply(response, puuid, geometry['uuid'])
            # success.append({"geometry": str(geometry), "responseDict": str(dictionary)})
            success.append({"geometry": str(geometry)})
            # print("SUCCESS: " + str(index) + " " + str(geometry))
            logger.info("SUCCESS: " + str(index) + " " + str(geometry))
        # except:
        except Exception as e:
            # e = sys.exc_info()[0]
            failed.append({"geometry": str(geometry), "error": str(e)})
            # failed.append(f"geometry: {geometry['uuid']} error: {e}\n")
            # print("FAILED: " + str(index) + " " + str(geometry))
            logger.info("FAILED: " + str(index) + " " + str(geometry) + " ERROR: " + str(e))
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


def save_ply(pcloud: PointCloud2, puuid: String, uuid: String):
    print("save_ply")
    logger.info("views.py make_task POST")
    try:
        endianness = "big" if pcloud.is_bigendian else "little"
        point_amount = pcloud.width * pcloud.height

        properties = ""
        for field in pcloud.fields:
            ptype = ""
            if field.datatype == 1:
                ptype = "int8"
            elif field.datatype == 2:
                ptype = "uint8"
            elif field.datatype == 3:
                ptype = "int16"
            elif field.datatype == 4:
                ptype = "uint16"
            elif field.datatype == 5:
                ptype = "int32"
            elif field.datatype == 6:
                ptype = "uint32"
            elif field.datatype == 7:
                ptype = "float32"
            elif field.datatype == 8:
                ptype = "float64"
            else:
                continue
            properties += f"property {ptype} {field.name}\n"

        header = f"ply\nformat binary_{endianness}_endian 1.0\nelement vertex {point_amount}\n{properties}end_header\n"

        '''
        Path(f"plys/{puuid}").mkdir(parents=True, exist_ok=True)
        file = open(f"plys/{puuid}/{uuid}", "wb")
        file.write(header.encode('utf-8'))
        file.write(pcloud.data)
        '''

        # https://docs.djangoproject.com/en/4.0/topics/files/

        file_path = 'storage/media/pointclouds/ply/' + puuid + '/' + uuid + '.ply'
        # file_path = settings.MEDIA_ROOT + 'pointclouds/ply/' + puuid + '/' + uuid + '.ply'

        logger.info("file_path " + str(file_path))

        if not default_storage.exists(file_path):
            file_content = ContentFile(header.encode('utf-8') + pcloud.data)
            default_storage.save(file_path, file_content)

    except Exception as e:
        print(e)
