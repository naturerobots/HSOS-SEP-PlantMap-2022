# 3D-View

## Overview

| Name                                                                | HTTP | URL                                                                               |   |   |
|---------------------------------------------------------------------|------|-----------------------------------------------------------------------------------|---|---|
| [Get list of 3d meta plant information](#3d-meta-plant-information-list) | GET  | `/companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d-scene/` |   |   |

## 3d meta plant information list

Send a GET request to this endpoint to get the Plant information.
The response contains two elements.
Firstly an array called plants, which contains informations about every plant in the bed.
Secondly an global elements which describes center position of the bed.

The plants array only contains plants for which the pointclouds are in the `django/storage/media/pointclouds/ply` folder.
The pointcloud of a plant can be loaded by the url given in the plants array.

**Request**: `/companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d-scene/`  
**Response** `200 Ok`, `404 Not Found`, `400 Bad Request`

Example response:

```json
{
"plants": [
      {
          "geometryUUID": "a671dab73f9844b280ac4d36f0314ad5",
          "measurementUUID": "8374c5058da64b73a7520955fc0c65fd",
          "url": "http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/a671dab73f9844b280ac4d36f0314ad5.ply",
          "name": "crop 16",
          "locationDescription": 1,
          "type": "mangold",
          "position": {
              "x": "-2.0091417",
              "y": "0.0038527877",
              "z": "-0.817174"
          },
          "health": [
              {
                  "type": "water",
                  "loglevel": 2,
                  "shortcut": "w"
              },
              {
                  "type": "nutrients",
                  "loglevel": 1,
                  "shortcut": "n"
              },
              {
                  "type": "diseases",
                  "loglevel": 3,
                  "shortcut": "d"
              }
          ],
          "yield": 705.1650603082642,
          "status": "vegetating",
          "harvest": "4 Weeks",
          "progress": "0.9351895742166416"
      }
  ],
  "global": {
      "position": {
          "x": "-1.9149369",
          "y": "-0.05081649",
          "z": "-0.8281588"
      }
  }
}
```
