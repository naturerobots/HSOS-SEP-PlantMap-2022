from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Company'
        managed = True

    def __str__(self):
        return self.name


class Garden(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    image_path = models.CharField(max_length=100, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Garden'
        managed = True

    def __str__(self):
        return self.name


class Coordinate(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    garden = models.ForeignKey(Garden, related_name='garden_coordinates', on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'Coordinates'


class Bed(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=32, null=True)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Bed'
        managed = True

    def __str__(self):
        return self.uuid


class CompanyPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.CharField(max_length=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'CompanyPermission'
        managed = True


class GardenPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.CharField(max_length=1)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'GardenPermission'
        managed = True
