from django.contrib import admin

from .models import Company, Garden, User

# Register your models here.
admin.site.register(Garden)
admin.site.register(Company)
admin.site.register(User)
