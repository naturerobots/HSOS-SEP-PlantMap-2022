import base64
import os
import re
from http.client import HTTPResponse
from uuid import uuid4

from rest_framework.decorators import api_view
from restapi.models import *
from restapi.serializer import CoordinateSerializer
from restapi.util.auth import isCompanyAdmin, isCompanyUser, isGardenAdmin, isGardenUser
from restapi.util.company_gardens import *

from django.http import *


# /companies
@api_view(['GET', 'POST'])
def companies(request):

    # GET: Endpoint that returns all companies a user has permissions on
    if request.method == 'GET':
        return getCompanies(request)

    # POST: Endpoint to create a new company
    elif request.method == 'POST':
        return createCompany(request)


# /gardens
# Endpoint that returns all gardens a user has permissions on
@api_view(['GET'])
def userGardens(request):

    try:
        gardenPermissions = GardenPermission.objects.filter(user=request.user)
        companyPermissions = CompanyPermission.objects.filter(user=request.user)
    except:
        return HttpResponseBadRequest()

    gardens = []

    for p in gardenPermissions.iterator():
        gardens.append(p.garden)

    for p in companyPermissions.iterator():
        try:
            companyGardens = Garden.objects.filter(company=p.company)
        except:
            continue
        for g in companyGardens.iterator():
            gardens.append(g)

    serializer = GardenSerializer(gardens, many=True)
    return JsonResponse(serializer.data, safe=False)


# /companies/{company_id}
@api_view(['GET', 'DELETE'])
def companyView(request, company_id: int):

    if request.method == 'GET':
        return getCompany(request, company_id)

    elif request.method == 'DELETE':
        return deleteCompany(request, company_id)


# /companies/{company_id}/gardens
@api_view(['GET', 'POST'])
def gardens(request, company_id: int):

    # GET: Endpoint that returns all gardens of the requested company the user has permissions on
    if request.method == 'GET':
        return getGardens(request, company_id)

    # POST: Endpoint to create a new garden
    elif request.method == 'POST':
        return createGarden(request, company_id)


# /companies/{company_id}/gardens/{garden_id}
@api_view(['GET', 'DELETE'])
def gardenView(request, company_id: int, garden_id: int):

    if request.method == 'GET':
        return getGarden(request, company_id, garden_id)

    elif request.method == 'DELETE':
        return deleteGarden(request, company_id, garden_id)


# TODO consider using class based views, for improved separation
@api_view(['GET', 'POST'])
def imageView(request, company_id: int, garden_id: int):

    if request.method == 'POST':
        return uploadImage(request, company_id, garden_id)

    elif request.method == 'GET':
        return getImage(request, company_id, garden_id)


def uploadImage(request, company_id, garden_id):

    if not 'coordinates' in request.data or not 'image' in request.data:
        return HttpResponseBadRequest()

    # Check if requesting user has admin permissions on garden
    if not isGardenAdmin(garden_id, request.user.username) and not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    # split image string to get file extension and raw bytes
    imageInfo, imageData = request.data['image'].split(',')
    infos = re.split(':|/|;', imageInfo)

    # TODO add env variable for storage location
    path = "/workdir/django/storage/images"
    if not os.path.exists(path):
        os.mkdir(path)

    # create unique file name
    if infos[2] != 'png':
        return HttpResponseBadRequest('We currently only support PNGs')
    filename = f"{path}/{uuid4()}.png"

    # decode bytes
    try:
        with open(filename, 'wb') as image:
            image.write(base64.b64decode(imageData))
    except FileNotFoundError:
        return HttpResponseBadRequest("Wrong format of image string in request")

    try:
        garden = Garden.objects.get(pk=garden_id)
    except Garden.DoesNotExist:
        return HttpResponseBadRequest(f"Garden number {garden_id} does not exists")
    garden.image_path = filename
    garden.save()

    for position in request.data['coordinates']:
        # if coordinates already exist just update, else create new ones
        try:
            coordinate = Coordinate.objects.get(name=position['name'], garden=garden_id)
            coordinate.latitude = position['latitude']
            coordinate.longitude = position['longitude']
            coordinate.save()
        except Coordinate.DoesNotExist:
            try:
                Coordinate(garden=garden, **position).save()
            except TypeError:
                return HttpResponseBadRequest("Wrong format of the positions in requests")

    return HttpResponse(status=201)


def getImage(request, company_id, garden_id):

    # Check if requesting user is allowed to access the garden
    if (
        not isGardenUser(garden_id, request.user.username)
        and not isGardenAdmin(garden_id, request.user.username)
        and not isCompanyUser(company_id, request.user.username)
        and not isCompanyAdmin(company_id, request.user.username)
    ):
        return HttpResponseForbidden()

    try:
        garden = Garden.objects.get(pk=garden_id)
    except Garden.DoesNotExist:
        return HttpResponseNotFound()

    if garden.image_path is None:
        return HttpResponseNotFound('No image uploaded for this garden')

    with open(garden.image_path, 'rb') as image:
        image_string = 'data:image/png;base64,' + base64.b64encode(image.read()).decode('ASCII')

    coordinates = garden.garden_coordinates.all()

    coordinates = CoordinateSerializer(coordinates, many=True).data

    return JsonResponse({"image": image_string, "coordinates": coordinates})


# /companies/{company_id}/gardens/{garden_id}/widget
@api_view(['GET', 'POST'])
def widgetView(request):

    if request.method == 'GET':
        return getWidget(request)

    elif request.method == 'POST':
        return createOrEditWidget(request)
