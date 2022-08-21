# Company & Garden Endpoints

## Overview

| Name                                                              | HTTP | URL                                                       |
| ----------------------------------------------------------------- | ---- | --------------------------------------------------------- |
| [Create company](#create-company)                                 | POST | /companies                                                |
| [Query companies](#query-companies)                               | GET  | /companies                                                |
| [Query specific company](#query-specific-company)                 | GET  | /companies/{company_id:int}                               |
| [Create garden of company](#create-garden-of-company)             | POST | /companies/{company_id:int}/gardens                       |
| [Query gardens of company](#query-gardens-of-company)             | GET  | /companies/{company_id:int}/gardens                       |
| [Query specific garden](#query-specific-garden)                   | GET  | /companies/{company_id:int}/gardens/{garden_id:int}       |
| [Upload image and coordinates](#upload-image-and-coordinates)     | POST | /companies/{company_id:int}/gardens/{garden_id:int}/image |
| [Download image and coordinates](#download-image-and-coordinates) | GET  | /companies/{company_id:int}/gardens/{garden_id:int}/image |

## Create company

**Request**:  `POST /companies`  
**Response**: `201 Created`, `404 Not Found`, `400 Bad Request`

Example request:

```json
{
 "name": "Demo-Company"
}
```

## Query companies

**Request**:  `GET /companies`  
**Response**: `200 Ok`, `404 Not Found`

Example response:

```json
[
 {
  "id": 1,
  "name": "Demo-Company"
 }
]
```

## Query specific company

**Request**:  `GET /companies/{company_id:int}`  
**Response**: `200 Ok`, `404 Not Found`

Example response:

```json
{
 "id": 1,
 "name": "Demo-Company"
}
```

## Create garden of company

**Request**:  `POST /companies/{company_id:int}/gardens`  
**Response**: `201 Created`, `404 Not Found`, `400 Bad Request`

Example request:

```json
{
 "name": "Demo-Garden-1"
}
```

## Query gardens of company

**Request**:  `GET /companies/{company_id:int}/gardens`  
**Response**: `200 Ok`, `404 Not Found`

Example response:

```json
[
 {
  "id": 1,
  "name": "Demo-Garden-1",
  "image_path": "/workdir/django/storage/images/2801cda6-6e3f-4028-8734-87f1f7eff067.png",
  "company": 1
 }
]
```

## Query specific garden

**Request**:  `GET /companies/{company_id:int}/gardens/{garden_id:int}`  
**Response**: `200 Ok`, `404 Not Found`

Example response:

```json
{
 "id": 1,
 "name": "Demo-Garden-1",
 "image_path": "/workdir/django/storage/images/2801cda6-6e3f-4028-8734-87f1f7eff067.png",
 "company": 1
}
```

## Upload image and coordinates

Uploading of an image from a garden, e.g. taken by drone, can be done via this
endpoint. In order to properly display it on a map, georeferencing is needed.
For this, at least 3 coordinates with the names `top_left`, `top_right` and `bottom_left` **must** be provided.

!!! info

    We currently only support the use of `.png` images.

**Request**:  `POST /companies/{company_id:int}/gardens/{garden_id:int}/image`  
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

**Request**: `GET /companies/{company_id:int}/gardens/{garden_id:int}/image`  
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
