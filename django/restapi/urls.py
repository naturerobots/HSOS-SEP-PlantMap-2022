from knox import views as knox_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login', views.LoginView.as_view(), name='knox_login'),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register', views.RegisterView.as_view()),
    path('users/<int:user_id>', views.getUser),
    path('companies/<int:company_id>', views.getCompany),
    path('companies/<int:company_id>/gardens', views.getGardens),
    path('companies/<int:company_id>/gardens/<int:garden_id>', views.getGarden),
    path('companies/<int:company_id>/gardens/<int:garden_id>/image', views.gardenImage),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds', views.getBeds),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants', views.getPlants),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants/<int:plant_id>/3d',
        views.getPlant3DImage,
    ),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/sensors', views.getSensors),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/sensors/<int:sensor_id>', views.getSensor
    ),
    path('beds/<str:uuid>/task', views.make_task),
]
