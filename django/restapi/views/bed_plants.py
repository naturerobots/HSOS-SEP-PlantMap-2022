import json
import logging
import string
import sys
from time import time

import grpc
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
from project_query_pb2 import ProjectQuery
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi import tasks
from restapi.models import *
from restapi.models import Garden
from restapi.util.auth import isCompanyAdmin, isCompanyUser, isGardenAdmin, isGardenUser
from transform_stamped_query_pb2 import TransformStampedQuery

from django.http import *
from django.urls import reverse

logger = logging.getLogger('django')

SERVER_URL = "seerep.naturerobots.de:5000"
options = [('grpc.max_receive_message_length', 100 * 1024 * 1024)]  # https://github.com/tensorflow/serving/issues/1382
channel = grpc.insecure_channel(SERVER_URL, options=options)

stub = metaOperations.MetaOperationsStub(channel)
stubLabel = labelService.LabelServiceStub(channel)
stubMeasurement = measurementService.MeasurementServiceStub(channel)
stubTf = tfService.TfServiceStub(channel)


# With the current dummy data this costs 100 gRPC-requests per bed. Seems like quite the DOS potential
# /companies/{company_id}/gardens/{garden_id}/beds
@api_view(['GET'])
def getBeds(request, company_id: int, garden_id: int):

    # Check if requesting user is allowed to access the garden
    if (
        not isGardenUser(garden_id, request.user.username)
        and not isGardenAdmin(garden_id, request.user.username)
        and not isCompanyUser(company_id, request.user.username)
        and not isCompanyAdmin(company_id, request.user.username)
    ):
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
            soil_humidity = []
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
                            plant_coords.append({"lat": lat, "lon": lon, "plant_id": plant.uuid})
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
                        soil_humidity.append(measurement.data["humidity"].double_data)

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
            soil_humidity = float(sum(soil_humidity)) / float(len(soil_humidity))
            harvest = int((float(sum(harvest)) / float(len(harvest))) / 604800)
            pyield = float(sum(pyield)) / float(len(pyield))
            phealth = []
            for hkey, hval in health.items():
                phealth.append({"type": hkey, "loglevel": int((float(sum(hval)) / float(len(hval))))})
            plants_url = reverse(
                'plants-resource', kwargs={'company_id': company_id, 'garden_id': garden_id, 'bed_id': bed.id}
            )

            avg_plant_lat = None
            avg_plant_lon = None
            if len(plant_coords) > 0:
                avg_plant_lat = float(sum(i['lat'] for i in plant_coords)) / len(plant_coords)
                avg_plant_lon = float(sum(i['lon'] for i in plant_coords)) / len(plant_coords)

            data = json.dumps(
                {
                    "id": bed.id,
                    "plant": plant_type,
                    "variety": variety,
                    "plants": request.build_absolute_uri(plants_url),
                    "soil_humidity": soil_humidity,
                    "harvest": f"{harvest} week",
                    "yield": pyield,
                    "health": phealth,
                    "plant_coords": plant_coords,
                    "avg_plant_lat": avg_plant_lat,
                    "avg_plant_lon": avg_plant_lon,
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
    if (
        not isGardenUser(garden_id, request.user.username)
        and not isGardenAdmin(garden_id, request.user.username)
        and not isCompanyUser(company_id, request.user.username)
        and not isCompanyAdmin(company_id, request.user.username)
    ):
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
        soil_humidity = 0.0
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
                soil_humidity = measurement.data["humidity"].double_data

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
            "bed_id": bed.id,
            "plant": plant_type,
            "variety": variety,
            "soil_humidity": soil_humidity,
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
