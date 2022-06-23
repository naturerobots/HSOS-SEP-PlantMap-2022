from django.contrib import admin

from .models import Bed, Company, Garden

admin.site.register(Company)
admin.site.register(Garden)
admin.site.register(Bed)
