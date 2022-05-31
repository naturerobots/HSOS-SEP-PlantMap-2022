from django.contrib import admin

from .models import Company, Garden, User

admin.site.register(Garden)
admin.site.register(Company)
admin.site.register(User)
