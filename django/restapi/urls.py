from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.list_projects),
    # path('<str:uuid>', views.list_project_detials),
    path('login', views.login),
    path('register', views.register),
    path('users/<str:user_id>', views.getUsers),
    path('companies/<str:company_id>', views.getCompanies),
    path('companies/<str:company_id>/gardens', views.getGardens),
    path('companies/<str:company_id>/gardens/<str:garden_id>', views.getGardenInfo),
    path('companies/<str:company_id>/gardens/<str:garden_id>/image', views.gardenImage),
    path('companies/<str:company_id>/gardens/<str:garden_id>/plants', views.getPlants),
    path('companies/<str:company_id>/gardens/<str:garden_id>/beds', views.getBeds),
    path('companies/<str:company_id>/gardens/<str:garden_id>/beds/<str:bed_id>', views.getBedInfo),
    path('companies/<str:company_id>/gardens/<str:garden_id>/beds/<str:bed_id>/3d', views.getBed3dImage),
    path('companies/<str:company_id>/gardens/<str:garden_id>/sensors', views.getSensors),
    path('companies/<str:company_id>/gardens/<str:garden_id>/sensors/<str:sensor_id>', views.getSensorInfo),
]
