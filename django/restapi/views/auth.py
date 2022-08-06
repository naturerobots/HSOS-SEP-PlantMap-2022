from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.serializer import UserSerializer
from restapi.util.auth import *

from django.contrib.auth import login
from django.http import *


# /login
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


# /register
class RegisterView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            authserializer = AuthTokenSerializer(data=request.data)
            if authserializer.is_valid():
                user = authserializer.validated_data['user']
                login(request, user)
                return super(RegisterView, self).post(request, format=None)
            return Response(authserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint to give a user permissions for a company
@api_view(['POST'])
def createCompanyPermissionView(request, company_id: int):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isCreatePermissionRequestValid(request):
        return HttpResponseBadRequest()

    inputData = json.loads(request.body)

    if not createCompanyPermission(company_id, inputData['user_id'], inputData['permission']):
        return HttpResponseBadRequest()

    return HttpResponse(status=201)


# Endpoint to remove a users permissions for a company
@api_view(['POST'])
def removeCompanyPermissionView(request, company_id: int):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isRemovePermissionRequestValid(request):
        return HttpResponseBadRequest()

    if not removeCompanyPermission(company_id, json.loads(request.body)['user_id']):
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


# Endpoint to give a user permissions for a garden
@api_view(['POST'])
def createGardenPermissionView(request, company_id: int, garden_id: int):

    # Check if requesting user has admin permissions on garden or company
    if not isGardenAdmin(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isCreatePermissionRequestValid(request):
        return HttpResponseBadRequest()

    inputData = json.loads(request.body)

    if not createGardenPermission(garden_id, inputData['user_id'], inputData['permission']):
        return HttpResponseBadRequest()

    return HttpResponse(status=201)


# Endpoint to remove a users permissions for a garden
@api_view(['POST'])
def removeGardenPermissionView(request, company_id: int, garden_id: int):

    # Check if requesting user has admin permissions on garden or company
    if not isGardenAdmin(garden_id, request.user.id) and not isCompanyAdmin(company_id, request.user.id):
        return HttpResponseForbidden()

    if not isRemovePermissionRequestValid(request):
        return HttpResponseForbidden()

    if not removeGardenPermission(garden_id, json.loads(request.body)['user_id']):
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


# /user
@api_view(['GET'])
def getUser(request):

    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data, safe=False)
