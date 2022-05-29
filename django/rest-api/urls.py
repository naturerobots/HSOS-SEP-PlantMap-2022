from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.list_projects),
    path('task', views.make_task),
    path('<str:uuid>', views.list_project_detials),
]
