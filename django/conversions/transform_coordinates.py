import numpy as np
import pymap3d.ned as pymap
from plyfile import PlyData
from scipy.spatial.transform import Rotation


def plantLocationOffset(projectUUID, geometryUUID):
    try:
        with open("/workdir/django/plys/" + projectUUID + "/" + geometryUUID + ".ply", "rb") as file:
            plydata = PlyData.read(file)
            # get an estimate of a plant's center, by taking the averge x and y
            x_avg = np.average(plydata.elements[0].data['x'])
            y_avg = np.average(plydata.elements[0].data['y'])
            return np.array([x_avg, y_avg, 0])
    except FileNotFoundError:
        return None


def transformLocation(translation, rotation, location):
    rotation = Rotation.from_quat(rotation)
    return rotation.apply(location + translation)


def locationToll(lat0, long0, point):
    return pymap.ned2geodetic(point[1], point[0], 0, lat0, long0, 0)


def llOfPlant(projectUUID: str, geometryUUID: str, lat0: float, long0: float, translation, rotation):
    plantLocation = plantLocationOffset(projectUUID, geometryUUID)
    if plantLocation is not None:
        locationTransformed = transformLocation(translation, rotation, np.transpose(plantLocation))
        return locationToll(lat0, long0, locationTransformed)
    else:
        return None
