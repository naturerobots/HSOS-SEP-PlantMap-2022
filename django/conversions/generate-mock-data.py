# Should be removed, when the conversions are integrated into the API
import sys

sys.path.append(r'../../build/gRPC/')
import json

import grpc
import meta_operations_service_pb2_grpc as metaOperations
import numpy as np
from project_query_pb2 import ProjectQuery
from transform_coordinates import llOfPlant

# example translation
translation = np.array([0, 0, 0])
rotation = np.array([0.0, 0.0, -0.4959135, 0.8683719])
latitude = 52.317118
longitude = 7.630613

SERVER_URL = "seerep.naturerobots.de:5000"
channel = grpc.insecure_channel(SERVER_URL)

stub = metaOperations.MetaOperationsStub(channel)
projectDetails = stub.GetProjectDetails(ProjectQuery(projectuuid="e1ef73b1258b475a996d2b72924c27ac"))

uuidList = [projectDetails.geometries[x].uuid for x in range(len(projectDetails.geometries))]

data = []
keys = ["name", "lat", "lng"]
for i, uuid in enumerate(uuidList):
    try:
        tmp = llOfPlant("e1ef73b1258b475a996d2b72924c27ac", uuid, latitude, longitude, translation, rotation)
        if tmp is not None:
            values = [str(i), tmp[0], tmp[1]]
            data.append(dict(zip(keys, values)))
    except FileNotFoundError:
        pass

with open('sensorMockData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
