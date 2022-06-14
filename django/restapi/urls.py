from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('users/<int:user_id>', views.getUsers),
    path('companies/<int:company_id>', views.getCompany),
    path('companies/<int:company_id>/gardens', views.getGardens),
    path('companies/<int:company_id>/gardens/<int:garden_id>', views.getGardenInfo),
    path('companies/<int:company_id>/gardens/<int:garden_id>/image', views.gardenImage),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds', views.getBeds),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants', views.getPlants),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants/<int:plant_id>/3d',
        views.getBed3dImage,
    ),
    path('companies/<int:company_id>/gardens/<int:garden_id>/sensors', views.getSensors),
    path('companies/<int:company_id>/gardens/<int:garden_id>/sensors/<int:sensor_id>', views.getSensorInfo),
]
