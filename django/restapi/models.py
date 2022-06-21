from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Company'
        managed = True

    def __str__(self):
        return self.name


class Garden(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Garden'
        managed = True

    def __str__(self):
        return self.name


class Bed(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=32, null=True)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Bed'
        managed = True

    def __str__(self):
        return self.name
