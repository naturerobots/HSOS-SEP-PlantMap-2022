import numpy as np
import pymap3d.ned as pymap
from numpy import ndarray
from plyfile import PlyData
from scipy.spatial.transform import Rotation


def plantLocationOffset(projectUUID, geometryUUID, dimensions=2):
    try:
        with open("storage/media/pointclouds/ply/" + projectUUID + "/" + geometryUUID + ".ply", "rb") as file:
            plydata = PlyData.read(file)
            # get an estimate of a plant's center, by taking the averge x, y and z, dependent on the dimensions

            x_avg = 0
            y_avg = 0
            z_avg = 0

            if dimensions == 1:
                x_avg = np.average(plydata.elements[0].data['x'])
            elif dimensions == 2:
                x_avg = np.average(plydata.elements[0].data['x'])
                y_avg = np.average(plydata.elements[0].data['y'])
            elif dimensions == 3:
                x_avg = np.average(plydata.elements[0].data['x'])
                y_avg = np.average(plydata.elements[0].data['y'])
                z_avg = np.average(plydata.elements[0].data['z'])
            else:
                raise Exception("dimensions can only be 1,2 or 3 but it is: " + str(dimensions))

            return np.array([x_avg, y_avg, z_avg])
    except FileNotFoundError:
        return None


def transformLocation(translation, rotation, location):
    rotation = Rotation.from_quat(rotation)
    return rotation.apply(location + translation)


def locationToll(lat0, long0, point):
    return pymap.ned2geodetic(point[1], point[0], 0, lat0, long0, 0)


def llOfPlant(projectUUID: str, geometryUUID: str, lat0: float, long0: float, translation: ndarray, rotation: ndarray):
    plantLocation = plantLocationOffset(projectUUID, geometryUUID)
    if plantLocation is not None:
        locationTransformed = transformLocation(translation, rotation, np.transpose(plantLocation))
        return locationToll(lat0, long0, locationTransformed)
    else:
        return None
