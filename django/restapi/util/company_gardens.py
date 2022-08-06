import json

from restapi.models import *
from restapi.util.auth import (
    createCompanyPermission,
    isCompanyAdmin,
    isCompanyUser,
    isCreateCompanyOrGardenRequestValid,
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
    if not createCompanyPermission(company.id, request.user.id, 'a'):
        Company.objects.delete(company)
        return HttpResponseBadRequest()

    return JsonResponse({'id': company.id})


# Endpoint that returns all gardens of the requested company the user has permissions on
def getGardens(request, company_id):

    # Check if requesting user is allowed to access company
    userIsCompanyAdmin = isCompanyAdmin(company_id, request.user.id)
    if not isCompanyUser(company_id, request.user.id) and not userIsCompanyAdmin:
        return HttpResponseForbidden()

    try:
        company = Company.objects.get(id=company_id)
        gardens = Garden.objects.filter(company=company)
    except:
        return HttpResponseBadRequest()

    # Company admin can access all gardens
    if userIsCompanyAdmin:
        serializer = GardenSerializer(gardens, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Check company user permissions on each garden
    authorizedGardens = []
    for g in gardens.iterator():
        if GardenPermission.objects.filter(user=request.user, garden=g).count() > 0:
            authorizedGardens.append(g)

    serializer = GardenSerializer(authorizedGardens, many=True)
    return JsonResponse(serializer.data, safe=False)


# Endpoint to create a new garden
def createGarden(request, company_id):

    # Check if requesting user has admin permissions on company
    if not isCompanyAdmin(company_id, request.user.id):
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
