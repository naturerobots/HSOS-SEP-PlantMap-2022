import json
import string
from http.client import HTTPResponse

from restapi.models import *
from restapi.serializer import CompanyPermissionSerializer, GardenPermissionSerializer

from django.http import *


# Endpoint to get user information
def getUser(request):

    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to edit user information
def editUser(request):

    if not request.body:
        return HttpResponseBadRequest()

    data = json.loads(request.body)
    if not data:
        return HttpResponseBadRequest()

    usr = request.user
    userEdited = False

    if 'username' in data:
        usr.username = data['username']
        userEdited = True

    if 'password' in data:
        usr.set_password(data['password'])
        userEdited = True

    if 'email' in data:
        usr.email = data['email']
        userEdited = True

    if 'first_name' in data:
        usr.first_name = data['first_name']
        userEdited = True

    if 'last_name' in data:
        usr.last_name = data['last_name']
        userEdited = True

    usr.save()

    if userEdited:
        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest()


# Authorization methods

# Checks if given permission is valid
def isPermissionValid(permission):
    if not permission or not permission in ['u', 'a']:
        return False
    return True


# Checks if given permission is user permission
def isUser(permission):
    if not permission or not permission in 'u':
        return False
    return True


# Checks if given permission is admin permission
def isAdmin(permission):
    if not permission or not permission in 'a':
        return False
    return True


# Checks if a HTTP request contains necessary keys and valid values
# to create a new permission in corresponding endpoints
def isCreatePermissionRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'username' in data or not 'permission' in data:
        return False

    if not isPermissionValid(data['permission']) or not data['username']:
        return False

    # Deny overwriting users own permissions
    if request.user.username == data['username']:
        return False

    return True


# Checks if a HTTP request contains necessary keys and valid values
# to remove a new permission in corresponding endpoints
def isRemovePermissionRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'username' in data:
        return False

    if not data['username']:
        return False

    # Deny removing users own permissions
    if request.user.username == data['username']:
        return False

    return True


# Checks if a HTTP request contains necessary keys and valid values
# to create a new company or garden in corresponding endpoints
def isCreateCompanyOrGardenRequestValid(request):

    if not request.body:
        return False

    data = json.loads(request.body)
    if not data or not 'name' in data:
        return False

    if not data['name']:
        return False

    return True


# Returns True, if username is allowed to access company_id
def isCompanyUser(company_id, username):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(username=username)
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        serializer = CompanyPermissionSerializer(companyPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    permission = serializer.data['permission']
    if not isUser(permission) and not isAdmin(permission):
        return False

    return True


# Returns True, if username is admin of company_id
def isCompanyAdmin(company_id, username):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(username=username)
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        serializer = CompanyPermissionSerializer(companyPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    if not isAdmin(serializer.data['permission']):
        return False

    return True


# Function to create a new company permission
# Returns True, if permission was created successfully
def createCompanyPermission(company_id, username, permission):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(username=username)

        # Filter for permission, update if exists or create new permission
        companyPermission = CompanyPermission.objects.filter(company=company, user=user).first()
        if companyPermission:
            companyPermission.permission = permission
            companyPermission.save()
        else:
            CompanyPermission.objects.create(permission=permission, company=company, user=user)

        return True
    except:
        return False


# Function to remove a users permissions for a company
# Returns True, if permission was deleted successfully or does not exist
def removeCompanyPermission(company_id, username):
    try:
        company = Company.objects.get(id=company_id)
        user = User.objects.get(username=username)

        # Filter for permission and delete it
        CompanyPermission.objects.filter(company=company, user=user).delete()

        return True
    except:
        return False


# Returns True, if username is allowed to access garden_id
def isGardenUser(garden_id, username):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(username=username)
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        serializer = GardenPermissionSerializer(gardenPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    permission = serializer.data['permission']
    if not isUser(permission) and not isAdmin(permission):
        return False

    return True


# Returns True, if username is admin of garden_id
def isGardenAdmin(garden_id, username):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(username=username)
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        serializer = GardenPermissionSerializer(gardenPermission)
    except:
        return False

    if not 'permission' in serializer.data:
        return False

    if not isAdmin(serializer.data['permission']):
        return False

    return True


# Function to create a new garden permission
# Returns True, if permission was created successfully
def createGardenPermission(garden_id, username, permission):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(username=username)

        # Filter for permission, update if it already exists or create a new permission
        gardenPermission = GardenPermission.objects.filter(garden=garden, user=user).first()
        if gardenPermission:
            gardenPermission.permission = permission
            gardenPermission.save()
        else:
            GardenPermission.objects.create(permission=permission, garden=garden, user=user)

        return True
    except:
        return False


# Function to remove a garden permission
# Returns True, if permission was deleted successfully or does not exist
def removeGardenPermission(garden_id, username):
    try:
        garden = Garden.objects.get(id=garden_id)
        user = User.objects.get(username=username)

        # Filter for permission and delete it
        GardenPermission.objects.filter(garden=garden, user=user).delete()

        return True
    except:
        return False
