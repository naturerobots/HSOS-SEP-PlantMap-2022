import logging
from os import listdir
from os.path import isfile, join

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

# @permission_classes([AllowAny])
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

    company = Company.objects.get(id=company_id)
    garden = Garden.objects.get(id=garden_id, company=company)
    bed = Bed.objects.get(id=bed_id, garden=garden)
    # projectUUID = 'e1ef73b1258b475a996d2b72924c27ac'
    projectUUID = str(bed)

    # logger.info(f"bedData: {bed}")

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

    return JsonResponse(result, safe=False)
