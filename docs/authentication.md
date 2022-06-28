# Authentication

## Endpoints

### `/login`

Send a POST request to this endpoint to login.
The request needs to contain a `username` and a `password` field either as form or json.

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

### `/register`

Requests and responses are the same as for `/login`,
but a new user is created with the provided username & password
and an error is returned if the username is already taken.

### `/logout` & `/logoutall`

These endpoints take an empty POST request.
With `/logout` the logged in user is logged out from the current session,
with `/logoutall` from all sessions.

## Token

The token returned from `/login` & `/register` needs to be send with every api-request
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
