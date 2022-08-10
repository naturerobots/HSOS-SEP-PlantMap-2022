# Company & Garden Endpoints

## Overview

| Name                                                              | HTTP | URL                            |
| ----------------------------------------------------------------- | ---- | ------------------------------ |
| [Upload image and coordinates](#upload-image-and-coordinates)     | POST | /gardens/{garden_id:int}/image |
| [Download image and coordinates](#download-image-and-coordinates) | GET  | /gardens/{garden_id:int}/image |

## Upload image and coordinates

Uploading of an image from a garden, e.g. taken by drone, can be done via this
endpoint. In order to properly display it on a map, georeferencing is needed.
For this, at least 3 coordinates with the names `top_left`, `top_right` and `bottom_left` **must** be provided.

!!! info

    We currently only support the use of `.png` images.

**Request**:  `POST /gardens/{garden_id:int}/image`  
**Response**: `201 Created`, `404 Not Found`, `400 Bad Request`

Example Request:

```json
{
 "image":"data:image/png;base64,iVBORw0KGg ...",
 "coordinates":[
    {
       "name":"top_left",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    },
    {
       "name":"top_right",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    },
    {
       "name":"bottom_left",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    }
 ]
}
```

## Download image and coordinates

**Request**: `GET /gardens/{garden_id:int}/image`  
**Response** `200 Ok`, `404 Not Found`, `400 Bad Request` 

Example Request:

```json
{
 "image":"data:image/png;base64,iVBORw0KGg ...",
 "coordinates":[
    {
       "name":"top_left",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    },
    {
       "name":"top_right",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    },
    {
       "name":"bottom_left",
       "latitude":52.31703822683545,
       "longitude":7.630155086517335
    }
 ]
}
```
