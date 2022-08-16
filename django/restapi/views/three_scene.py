import base64
import re
from os import listdir
from os.path import isfile, join

import numpy as np
from conversions.transform_coordinates import plantLocationOffset
from plyfile import PlyData
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from restapi.helpers.auth import (
    isCompanyAdmin,
    isCompanyUser,
    isGardenAdmin,
    isGardenUser,
)
from restapi.helpers.company_gardens import *
from restapi.models import *
from restapi.models import Garden

from django.http import *


# @permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def get3dPlants(request, company_id: int, garden_id: int, bed_id: int):

    # Get bed Hash

    projectUUID = 'e1ef73b1258b475a996d2b72924c27ac'
    localPath = 'storage/media/pointclouds/ply/' + str(projectUUID) + '/'
    externalPath = 'media/pointclouds/ply/' + str(projectUUID) + '/'
    url = "http://localhost:8000/" + externalPath

    onlyfiles = [f for f in listdir(localPath) if isfile(join(localPath, f))]

    plants = []

    totalX = []
    totalY = []
    totalZ = []

    for file in onlyfiles:
        geometryUUID = file[:-4]
        locationOffset = plantLocationOffset(projectUUID=projectUUID, geometryUUID=geometryUUID, dimensions=3)
        '''
        plant = {
            "geometryUUID": geometryUUID,
            "url": url + file,
            "name": "Swiss Chard",
            "locationDescription": "Row 12",
            "location": {
                "x": str(locationOffset[0]),
                "y": str(locationOffset[1]),
                "z": str(locationOffset[2]),
            },
            "health": {
                "disease": 1,
                "nutrient": 2,
                "watering": 3,
            },
            "yield": "N/A",
            "status": "Vegetating",
            "Harvest": "2 Weeks",
            "progress": 0.6,
        }
        '''

        totalX.append(locationOffset[0])
        totalY.append(locationOffset[1])
        totalZ.append(locationOffset[2])

        plant = {
            "geometryUUID": geometryUUID,
            "url": url + file,
            "name": "Swiss Chard",
            "locationDescription": "Row 12",
            "type": "11 Cluster",
            "position": {
                "x": str(locationOffset[0]),
                "y": str(locationOffset[1]),
                "z": str(locationOffset[2]),
            },
            "health": [
                {
                    "type": "type1",
                    "loglevel": 1,
                    "shortcut": "O",
                },
                {
                    "type": "type2",
                    "loglevel": 2,
                    "shortcut": "T",
                },
            ],
            "yield": "N/A",
            "status": "Vegetating",
            "harvest": "2 Weeks",
            "progress": "0.75",
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

    data = json.dumps(str(result))

    return JsonResponse(result, safe=False)
