from django.contrib import admin

from .models import Bed, Company, CompanyPermission, Garden, GardenPermission, Widget

admin.site.register(Company)
admin.site.register(Garden)
admin.site.register(Bed)
admin.site.register(CompanyPermission)
admin.site.register(GardenPermission)
admin.site.register(Widget)
