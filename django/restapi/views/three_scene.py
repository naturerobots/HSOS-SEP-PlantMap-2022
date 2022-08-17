import logging
from os import listdir
from os.path import isfile, join
from queue import Empty
from time import time

import numpy as np
from conversions.transform_coordinates import plantLocationOffset
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from restapi.models import Bed, Company, Garden

'''
from restapi.helpers.auth import (
    isCompanyAdmin,
    isCompanyUser,
    isGardenAdmin,
    isGardenUser,
)
from restapi.helpers.company_gardens import *
'''
from restapi.models import *
from restapi.models import Garden

from django.http import *

logger = logging.getLogger('django')

import grpc
import label_service_pb2_grpc as labelService
import measurement_service_pb2_grpc as measurementService
import meta_operations_service_pb2_grpc as metaOperations
import tf_service_pb2_grpc as tfService
from geometry_query_pb2 import GeometryQuery
from instance_query_pb2 import InstanceQuery
from project_query_pb2 import ProjectQuery

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)
stubLabel = labelService.LabelServiceStub(channel)
stubMeasurement = measurementService.MeasurementServiceStub(channel)
stubTf = tfService.TfServiceStub(channel)


@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def get3dPlants(request, company_id: int, garden_id: int, bed_id: int):

    '''
    if (
        not isGardenUser(garden_id, request.user.username)
        and not isGardenAdmin(garden_id, request.user.username)
        and not isCompanyUser(company_id, request.user.username)
        and not isCompanyAdmin(company_id, request.user.username)
    ):
        return HttpResponseForbidden()
    '''

    # Get bed Hash

    # curl -X POST http://localhost:8000/companies/1/gardens/1/beds/1/3d-scene/ -H "Authorization: Token 9e57569be21f2c4cda8d26e41684fedfa447a51f86e501b03cedd219cb7f3057"

    company = Company.objects.get(id=company_id)
    garden = Garden.objects.get(id=garden_id, company=company)
    bed = Bed.objects.get(id=bed_id, garden=garden)
    # projectUUID = 'e1ef73b1258b475a996d2b72924c27ac'
    # projectUUID = bed.uuid
    bedData = stub.GetProjectDetails(ProjectQuery(projectuuid=bed.uuid))

    # logger.info(f"bedData: {bedData}")

    localPath = 'storage/media/pointclouds/ply/' + str(bed.uuid) + '/'
    externalPath = 'media/pointclouds/ply/' + str(bed.uuid) + '/'
    url = "http://localhost:8000/" + externalPath

    onlyfiles = [f for f in listdir(localPath) if isfile(join(localPath, f))]

    plants = []

    totalX = []
    totalY = []
    totalZ = []

    for file in onlyfiles:
        geometryUUID = file[:-4]

        # Get Geometry and Measurement Meta Data of the Pointcloud
        geometryMeta = Empty
        measurementMeta = Empty
        for g in bedData.geometries:
            if g.uuid == geometryUUID and g.type == "pointcloud":
                geometryMeta = g
                break

        for g in bedData.geometries:
            if g.name == geometryMeta.name and g.type == "measurement":
                measurementMeta = g
                break

        logger.info("GEOMETRYMETA: " + str(geometryMeta))
        logger.info("MEASUREMENTMETA: " + str(measurementMeta))

        # Get Measurement
        measurement = stubMeasurement.GetMeasurementByUUID(
            GeometryQuery(projectuuid=bed.uuid, geometryuuid=measurementMeta.uuid)
        )
        logger.info("MEASUREMENT: " + str(measurement))

        measurementUUID = measurementMeta.uuid
        plantUrl = url + file
        name = geometryMeta.name
        locationDescription = ""
        plantType = "Error"
        health = []
        plantYield = ""
        status = ""
        harvest = ""
        progress = ""

        # Status
        if "status" in measurement.data:
            logger.info("measurement.data['status']: " + str(measurement.data["status"]))
            status = measurement.data["status"].string_data

        # Progress
        if "growth_state" in measurement.data:
            progress = measurement.data["growth_state"].double_data

        # Yield
        if "approx_yield" in measurement.data:
            plantYield = measurement.data["approx_yield"].double_data

        # Health
        for i in range(3):
            if all(key in measurement.data for key in (f"health_{i}_type", f"health_{i}_level")):
                htype = measurement.data[f"health_{i}_type"].string_data
                hlevel = measurement.data[f"health_{i}_level"].int64_data
                health.append({"type": htype, "loglevel": hlevel})

        instance = stubLabel.GetInstance(InstanceQuery(projectuuid=bed.uuid, instanceuuid=geometryMeta.labels[0]))

        plantType = instance.name

        if "planting_date" in instance.attributes and "growth_state" in measurement.data:
            planting_date: int = instance.attributes["planting_date"].int64_data
            growth_state: float = measurement.data["growth_state"].double_data

            harvest = int(((time() - planting_date) * (1.0 - growth_state)) / 604800.0)

        locationOffset = plantLocationOffset(projectUUID=bed.uuid, geometryUUID=geometryUUID, dimensions=3)

        totalX.append(locationOffset[0])
        totalY.append(locationOffset[1])
        totalZ.append(locationOffset[2])

        plant = {
            "geometryUUID": geometryUUID,
            "measurementUUID": measurementUUID,
            "url": plantUrl,
            "name": name,
            "locationDescription": "Row 12",
            "type": plantType,
            "position": {
                "x": str(locationOffset[0]),
                "y": str(locationOffset[1]),
                "z": str(locationOffset[2]),
            },
            "health": health,
            "yield": plantYield,
            "status": status,
            "harvest": str(harvest) + " Weeks",
            "progress": str(progress),
        }

        # plants[geometryUUID]=plant
        plants.append(plant)

    result = {
        "plants": plants,
        "global": {
            "position": {
                "x": str(np.average(totalX)),
                "y": str(np.average(totalY)),
                "z": str(np.average(totalZ)),
            }
        },
    }

    return JsonResponse(result, safe=False)
