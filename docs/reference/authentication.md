# Authentication

## Endpoints

### Overview

| Name                                                      | HTTP | URL                  |
| --------------------------------------------------------- | ---- | -------------------- |
| [Login existing account](#login-existing-account)         | POST | /login               |
| [Register new account](#register-new-account)             | POST | /register            |
| [Logout current user](#logout-current-user)               | POST | /logout & /logoutall |
| [Query current user](#query-current-user)                 | GET  | /user                |
| [Edit current user](#edit-current-user)                   | PUT  | /user                |
| [Save current user widgets](#save-current-user-widgets)   | POST | /user/widgets        |
| [Query current user widgets](#query-current-user-widgets) | GET  | /user/widgets        |

### Login existing account

Send a POST request to this endpoint to login.
The request needs to contain a `username` and a `password` field either as form or json.

**Request**:  `POST /login`  
**Response**: `200 Ok`, `400 Bad Request`

Example request:

```json
{
  "username": "testuser123",
  "password": "7Gq^7Mjwgi%#DcHj22$C"
}
```

Example response:

```json
{
  "expiry": "2022-06-28T21:20:47.530747Z",
  "token": "83a386188e12a075682c86ae9a760a6f9e7402c468ac29a33f898663c69897d5"
}
```

### Register new account

Responses are the same as for `/login`,
but requests need to supply a `first_name` and a `last_name` as well.
A new user is created with the provided information
and an error is returned if the username is already taken.

**Request**:  `POST /register`  
**Response**: `201 Created`, `400 Bad Request`

Example request:

```json
{
 "username": "testuser1234",
 "password": "7Gq^7Mjwgi%#DcHj22$C",
 "first_name": "first",
 "last_name": "last"
}
```

### Logout current user

These endpoints take an empty POST request.
With `/logout` the logged in user is logged out from the current session,
with `/logoutall` from all sessions.

**Request 1**:  `POST /logout`  
**Request 2**:  `POST /logoutall`  
**Response**: `200 Ok`, `400 Bad Request`

### Query current user

An empty GET request returns information about the currently logged in user.

**Request**:  `GET /user`  
**Response**: `200 Ok`

Example response:

```json
{
 "username": "testuser1234",
 "first_name": "first",
 "last_name": "last",
 "date_joined": "2022-07-12T12:49:31.010300Z",
 "last_login": "2022-07-19T11:35:55.158069Z"
}
```

### Edit current user

Send a PUT request to change the information of the current user.
All fields are optional.

**Request**:  `PUT /user`  
**Response**: `200 Ok`

Example request:

```json
{
 "username": "testuser1234",
 "first_name": "first",
 "last_name": "last",
 "password": "supersecurepasswordTM",
 "email": "testuser1234@example.com"
}
```

### Save current user widgets

A POST request with an arbitrary JSON payload can be sent
to this endpoint to save it for later retrieval.

**Request**:  `POST /user/widgets`  
**Response**: `201 Created`, `400 Bad Request`

Example request:

```json
{
 "widgets": [
  "3d-table",
  "3d-map",
  "weather",
  "soil-parameter",
  "garden-map",
  "notifications",
  "crops-map",
  "crops-table"
 ]
}
```

### Query current user widgets

An empty GET request returns the arbitrary JSON config that was previously saved.

**Request**:  `GET /user/widgets`  
**Response**: `200 Ok`, `400 Bad Request`

Example response:

```json
{
 "widgets": [
  "3d-table",
  "3d-map",
  "weather",
  "soil-parameter",
  "garden-map",
  "notifications",
  "crops-map",
  "crops-table"
 ]
}
```

## Token

The token returned from `/login` & `/register` **needs to be send with every api-request**
in the [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) header
with `Token` as a prefix.

Example Authorization header:

```header
Authorization: Token 83a386188e12a075682c86ae9a760a6f9e7402c468ac29a33f898663c69897d5
```

## Backend

Authorization can be disabled for an endpoint for testing in the views.py by annotating the function with `@permission_classes([AllowAny])`
([Example here, uncomment the line](https://github.com/naturerobots/HSOS-SEP-PlantMap-2022/blob/2d73e5f4360c42e71dcbb0cb546c3fd9a6d2dd05/django/restapi/views.py#L42)).

The logged-in user is accessible in the backend via `request.user`.
