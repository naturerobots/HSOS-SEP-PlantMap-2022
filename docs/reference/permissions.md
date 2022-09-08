# Permission System

## Basics

The permission system consists of two database tables CompanyPermission and GardenPermission.
Each row in the table holds the reference to either a company or garden, the user and the users permission.
The permission is represented by a single char. Possible permissions are described in the next section.
In addition, each row in the table has a unique number as a primary-key.

Example rows in table CompanyPermission:

|id (PK)|company_id (FK)|user_id (FK)|permission|
|:-----:|:-------------:|:----------:|:--------:|
|   1   |       1       |      1     |     a    |
|   2   |       1       |      2     |     u    |

Example rows in table GardenPermission:

|id (PK)|garden_id (FK)|user_id (FK)|permission|
|:-----:|:------------:|:----------:|:--------:|
|   1   |       1      |      1     |     a    |
|   2   |       1      |      2     |     u    |

## Roles

The following roles exist:

- 'u': user; can read/access information from specified garden or company
- 'a': admin; full access on a specified garden or company

## Endpoints

### Overview

| Name                                                    | HTTP | URL                                                                  |
| ------------------------------------------------------- | ---- | -------------------------------------------------------------------- |
| [Create company permission](#create-company-permission) | POST | /companies/{company_id:int}/createPermission                         |
| [Remove company permission](#remove-company-permission) | POST | /companies/{company_id:int}/removePermission                         |
| [Create garden permission](#create-garden-permission)   | POST | /companies/{company_id:int}/gardens/{garden_id:int}/createPermission |
| [Remove garden permission](#remove-garden-permission)   | POST | /companies/{company_id:int}/gardens/{garden_id:int}/removePermission |

### Create company permission

Send a POST request to this endpoint to give a user permissions on the company specified in the URL.
The request body needs to contain a `username` and a `permission` field as json.

Only admins of the corresponding company can access this endpoint.

The following request with URL: `../companies/2/createPermission`
gives the user with username `testuser` admin permissions on the company with id `2`:

```json
{
  "username": "testuser",
  "permission": "a"
}
```

If a permission for this user and company already exists, it will be overwritten. Own permissions cannot be overwritten,
in order to prevent locking yourself out.

**Request**:  `POST /companies/{company_id:int}/createPermission`  
**Responses**:

- HTTP-201 (Created), if the permission was created successfully.
- HTTP-400 (Bad Request), if for example the permission was not sent with the request.
- HTTP-403 (Forbidden), if the requesting user is not admin of the company and thus cannot set permissions or
  if the user tries to overwrite own permissions.

### Remove company permission

Send a POST request to this endpoint to remove the permissions of a user to the company specified in the URL.
The request body needs to contain a `username` field as json.

Only admins of the corresponding company can access this endpoint.
Own permissions or those of the last admin cannot be removed.

The following request with URL: `../companies/2/createPermission`
removes the permissions for the user with username `testuser` on the company with id `2`:

```json
{
  "username": "testuser"
}
```

**Request**:  `POST /companies/{company_id:int}/removePermission`  
**Responses**:

- HTTP-200 (Ok), if the permission was deleted successfully or does not exist.
- HTTP-400 (Bad Request), if for example user_id was not sent with the request.
- HTTP-403 (Forbidden), if the requesting user is not admin of the company and thus cannot set permissions or
  if the user tries to remove own permissions.

### Create garden permission

Endpoint to give a user permissions on the garden specified in the URL.
Works the same as creating a permission for a company.

Only admins of the corresponding company or garden can access this endpoint.

**Request**:  `POST /companies/{company_id:int}/gardens/{garden_id:int}/createPermission`  
**Responses**: `201 Created`, `400 Bad Request`, `403 Forbidden`

### Remove garden permission

Endpoint to remove the permissions of a user to the garden specified in the URL.
Works the same as removing a permission for a company.

Only admins of the corresponding company or garden can access this endpoint.

**Request**:  `POST /companies/{company_id:int}/gardens/{garden_id:int}/removePermission`  
**Responses**: `200 Ok`, `400 Bad Request`, `403 Forbidden`
