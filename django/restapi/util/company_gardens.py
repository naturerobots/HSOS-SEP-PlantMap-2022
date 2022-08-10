import json
from urllib.request import HTTPBasicAuthHandler

from restapi.models import *
from restapi.serializer import CompanySerializer, GardenSerializer
from restapi.util.auth import (
    createCompanyPermission,
    isCompanyAdmin,
    isCompanyUser,
    isCreateCompanyOrGardenRequestValid,
    isGardenAdmin,
    isGardenUser,
)
from restapi.util.company_gardens import *

from django.http import *


# Endpoint that returns all companies a user has permissions on
def getCompanies(request):

    try:
        companyPermissions = CompanyPermission.objects.filter(user=request.user)
    except:
        return HttpResponseBadRequest()

    companies = []
    for p in companyPermissions.iterator():
        companies.append(p.company)

    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to create a new company
def createCompany(request):

    if not isCreateCompanyOrGardenRequestValid(request):
        return HttpResponseBadRequest()

    try:
        company = Company.objects.create(name=json.loads(request.body)['name'])
    except:
        return HttpResponseBadRequest()

    # Give the user admin permissions on new company
    # Delete company if permission could not be set successfully
    if not createCompanyPermission(company.id, request.user.username, 'a'):
        try:
            Company.objects.filter(id=company.id).delete()
        except:
            pass
        return HttpResponseBadRequest()

    return JsonResponse({'id': company.id})


# Endpoint to get a company
def getCompany(request, company_id):

    # Check if requesting user is allowed to access company
    if not isCompanyUser(company_id, request.user.username) and not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponseBadRequest()


# Endpoint to delete a company
def deleteCompany(request, company_id):

    # Check if requesting user is company admin
    if not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    try:
        Company.objects.filter(id=company_id).delete()
    except:
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


# Endpoint that returns all gardens of the requested company the user has permissions on
def getGardens(request, company_id):

    # Check if requesting user is allowed to access company
    if not isCompanyUser(company_id, request.user.username) and not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        gardens = Garden.objects.filter(company=company)
    except:
        return HttpResponseBadRequest()

    serializer = GardenSerializer(gardens, many=True)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to create a new garden
def createGarden(request, company_id):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    if not isCreateCompanyOrGardenRequestValid(request):
        return HttpResponseBadRequest()

    # Create new garden
    try:
        company = Company.objects.get(id=company_id)
        garden = Garden.objects.create(name=json.loads(request.body)['name'], company=company, image_path=None)
    except:
        return HttpResponseBadRequest()

    return JsonResponse({'id': garden.id})


# Endpoint to get a garden
def getGarden(request, company_id, garden_id):

    # Check if requesting user is allowed to access the garden
    if (
        not isGardenUser(garden_id, request.user.username)
        and not isGardenAdmin(garden_id, request.user.username)
        and not isCompanyUser(company_id, request.user.username)
        and not isCompanyAdmin(company_id, request.user.username)
    ):
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        garden = Garden.objects.get(id=garden_id, company=company)
    except:
        return HttpResponseBadRequest()

    serializer = GardenSerializer(garden)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to delete a garden
def deleteGarden(request, company_id, garden_id):

    # Check if requesting user is admin of company or garden
    if not isGardenAdmin(garden_id, request.user.username) and not isCompanyAdmin(company_id, request.user.username):
        return HttpResponseForbidden()

    try:
        Garden.objects.filter(id=garden_id).delete()
    except:
        return HttpResponseBadRequest()

    return HttpResponse(status=200)


def getWidget(request):

    try:
        widget = Widget.objects.filter(user=request.user).first()
    except:
        return HttpResponseBadRequest()

    if not widget:
        return JsonResponse({})
    else:
        return HttpResponse(json.dumps(widget.data), content_type="application/json")


def createOrEditWidget(request):

    if not request.body:
        return HttpResponseBadRequest()

    # Save widget settings
    try:
        widget = Widget.objects.filter(user=request.user).first()
        if widget:
            widget.data = json.loads(request.body)
            widget.save()
        else:
            Widget.objects.create(user=request.user, data=json.loads(request.body))
    except:
        return HttpResponseBadRequest()

    return HttpResponse(status=200)
