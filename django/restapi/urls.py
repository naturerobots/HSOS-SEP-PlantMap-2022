from knox import views as knox_views
from restapi.views import auth, bed_plants, company_gardens

from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login', auth.LoginView.as_view(), name='knox_login'),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register', auth.RegisterView.as_view()),
    path('companies', company_gardens.companies),
    path('user-info', auth.getUser),
    path('companies/<int:company_id>', company_gardens.getCompany),
    path('companies/<int:company_id>/createPermission', auth.createCompanyPermissionView),
    path('companies/<int:company_id>/removePermission', auth.removeCompanyPermissionView),
    path('companies/<int:company_id>/gardens', company_gardens.gardens),
    path('companies/<int:company_id>/gardens/<int:garden_id>', company_gardens.getGarden),
    path('companies/<int:company_id>/gardens/<int:garden_id>/createPermission', auth.createGardenPermissionView),
    path('companies/<int:company_id>/gardens/<int:garden_id>/removePermission', auth.removeGardenPermissionView),
    path('companies/<int:company_id>/gardens/<int:garden_id>/image', company_gardens.imageView),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds', bed_plants.getBeds),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants',
        bed_plants.getPlants,
        name='plants-resource',
    ),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d', bed_plants.getBed3DImage),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d',
        bed_plants.getBed3DImage,
    ),
    path('beds/<str:uuid>/task', bed_plants.make_task),
]
