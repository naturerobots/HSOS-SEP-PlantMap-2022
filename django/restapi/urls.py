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
    path('user', views.getUser),
    path('companies', views.getCompanies),
    path('companies/<int:company_id>', views.getCompany),
    path('companies/<int:company_id>/addPermission', views.addCompanyPermission),
    path('companies/<int:company_id>/removePermission', views.removeCompanyPermission),
    path('companies/<int:company_id>/gardens', views.getGardens),
    path('companies/<int:company_id>/gardens/<int:garden_id>', views.getGarden),
    path('companies/<int:company_id>/gardens/<int:garden_id>/addPermission', views.addGardenPermission),
    path('companies/<int:company_id>/gardens/<int:garden_id>/removePermission', views.removeGardenPermission),
    path('companies/<int:company_id>/gardens/<int:garden_id>/image', views.gardenImage),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds', views.getBeds),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/crops', views.getCrops),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d',
        views.getBed3DImage,
    ),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/sensors', views.getSensors),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/sensors/<int:sensor_id>', views.getSensor
    ),
    path('beds/<str:uuid>/task', views.make_task),
]
