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

### `/companies/{company_id}/createPermission`

Send a POST request to this endpoint to give a user permissions on the company specified in the URL.
The request body needs to contain a `user_id` and a `permission` field as json.

Only admins of the corresponding company can access this endpoint.

The following request with URL: ../companies/2/createPermission
gives the user with id '42' admin permissions on the company with id '2':

```json
{
  "user_id": "42",
  "permission": "a"
}
```

If a permission for this user and company already existed before, it will be deleted and a new one is created.
Own permissions cannot be overwritten.

Responses:

- HTTP-201 (Created), if the permission was created successfully.
- HTTP-400 (Bad Request), if for example the permission was not sent with the request.
- HTTP-403 (Forbidden), if the requesting user is not admin of the company and thus cannot set permissions or
  if the user tries to overwrite own permissions.

### `/companies/{company_id}/removePermission`

Send a POST request to this endpoint to remove the permissions of a user to the company specified in the URL.
The request body needs to contain a `user_id` field as json.

Only admins of the corresponding company can access this endpoint.
Own permissions or those of the last admin cannot be removed.

The following request with URL: ../companies/2/createPermission
removes the permissions for the user with id '42' on the company with id '2':

```json
{
  "user_id": "42"
}
```

Responses:

- HTTP-200 (Ok), if the permission was deleted successfully or does not exist.
- HTTP-400 (Bad Request), if for example user_id was not sent with the request.
- HTTP-403 (Forbidden), if the requesting user is not admin of the company and thus cannot set permissions or
  if the user tries to remove own permissions.

### `/companies/{company_id}/gardens/{garden_id}/createPermission`

Endpoint to give a user permissions on the garden specified in the URL.
Works the same as creating a permission for a company.

Only admins of the corresponding company or garden can access this endpoint.

### `/companies/{company_id}/gardens/{garden_id}/removePermission`

Endpoint to remove the permissions of a user to the garden specified in the URL.
Works the same as removing a permission for a company.

Only admins of the corresponding company or garden can access this endpoint.
