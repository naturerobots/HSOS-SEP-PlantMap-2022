from knox import views as knox_views

from django.urls import path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login', views.LoginView.as_view(), name='knox_login'),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register', views.RegisterView.as_view()),
    path('companies', views.companies),
    path('user-info', views.getUser),
    path('gardens/<int:garden_id>/image', views.imageView),
    path('companies/<int:company_id>', views.getCompany),
    path('companies/<int:company_id>/createPermission', views.createCompanyPermissionView),
    path('companies/<int:company_id>/removePermission', views.removeCompanyPermissionView),
    path('companies/<int:company_id>/gardens', views.gardens),
    path('companies/<int:company_id>/gardens/<int:garden_id>', views.getGarden),
    path('companies/<int:company_id>/gardens/<int:garden_id>/createPermission', views.createGardenPermissionView),
    path('companies/<int:company_id>/gardens/<int:garden_id>/removePermission', views.removeGardenPermissionView),
    path('companies/<int:company_id>/gardens/<int:garden_id>/image', views.gardenImage),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds', views.getBeds),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/plants',
        views.getPlants,
        name='plants-resource',
    ),
    path('companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d', views.getBed3DImage),
    path(
        'companies/<int:company_id>/gardens/<int:garden_id>/beds/<int:bed_id>/3d',
        views.getBed3DImage,
    ),
    path('beds/<str:uuid>/task', views.make_task),
]
