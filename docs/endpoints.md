# Endpoints

## General

### `/companies/<int:company_id>/gardens/<int:garden_id>/beds`

Accepts an empty GET request and returnes a streamed json response as seen below
with information about the beds in the specified garden.
The values are averaged from all the plants in the bed.

!!! info
    Due to the large amount of data that needs to be queried for this endpoint,
    a lot of gRPC requests need to be made to the SEEREP server, which might take a while.

    The amount of gRPC reqests can be calculated like this:
    `numBeds + 3 * numPlants` or `numBeds + 3 * numBeds * numPlantsPerBed`.

    For 6 beds with 33 plants each, 600 gRPC requests need to be send,
    which may take ~20 seconds, during which the response is streamed back.

Example response:

```json
{
 "beds": [
  {
   "id": 1,
   "location": "TODO",
   "plant": "mangold",
   "variety": "Lucullus",
   "plants": "http://localhost:8000/companies/1/gardens/1/beds/1/plants",
   "soil_humidty": 0.65,
   "harvest": "6 week",
   "yield": 451.1587423100285,
   "health": [
    {
     "type": "water",
     "loglevel": 1
    },
    {
     "type": "nutrients",
     "loglevel": 1
    },
    {
     "type": "diseases",
     "loglevel": 1
    }
   ]
  },
  {
   "id": 2,
   "location": "TODO",
   "plant": "mangold",
   "variety": "Lucullus",
   "plants": "http://localhost:8000/companies/1/gardens/1/beds/2/plants",
   "soil_humidty": 0.65,
   "harvest": "6 week",
   "yield": 451.1587423100285,
   "health": [
    {
     "type": "water",
     "loglevel": 1
    },
    {
     "type": "nutrients",
     "loglevel": 1
    },
    {
     "type": "diseases",
     "loglevel": 1
    }
   ]
  }
 ]
}
```

### `/companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants`

Accepts an empty GET request and returnes a json response with information
about the individual plants in the specified bed.
As seen below, the response looks similar to the one from the `beds` endpoint above,
but these values are per plant and not averages.

Example response:

```json
{
 "plants": [
  {
   "id": "25816c5842f14fe98b1ebc85a4908934",
   "bedid": 1,
   "location": "TODO",
   "plant": "mangold",
   "variety": "Lucullus",
   "soil_humidty": 0.0,
   "harvest": "10 week",
   "yield": 486.50339525240184,
   "health": [
    {
     "type": "water",
     "loglevel": 1
    },
    {
     "type": "nutrients",
     "loglevel": 1
    },
    {
     "type": "diseases",
     "loglevel": 2
    }
   ]
  },
  {
   "id": "5107b0de17984b038b4319ad431c9775",
   "bedid": 1,
   "location": "TODO",
   "plant": "weed",
   "variety": "Lucullus",
   "soil_humidty": 0.0,
   "harvest": "0 week",
   "yield": 324.1666937668429,
   "health": [
    {
     "type": "water",
     "loglevel": 1
    },
    {
     "type": "nutrients",
     "loglevel": 1
    },
    {
     "type": "diseases",
     "loglevel": 1
    }
   ]
  }
 ]
}
```

## Authentication

### `/login`, `/register`, `/logout`, `/logoutall` & `/user`

See [Authentication](/authentication).
