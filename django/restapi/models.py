import os
from dataclasses import fields
from turtle import position
from uuid import uuid4

from rest_framework import serializers

from django.contrib.auth.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined', 'last_login']
        # fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Company'
        managed = True

    def __str__(self):
        return self.name


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# Creates random filenames for garden images
def path_and_rename(path):
    filename = '{}.{}'.format(uuid4().hex, 'png')
    return os.path.join(path, filename)


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=100)

    class Meta:
        app_label = 'restapi'
        db_table = 'Image'


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


class Widget(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()

    class Meta:
        app_label = 'restapi'
        db_table = 'Widget'
        managed = True

    def __str__(self):
        return self.user


class Coordinate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    latitude = models.FloatField()
    longitude = models.FloatField()
    garden = models.ForeignKey(Garden, related_name='garden_coordinates', on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'Coordinates'


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        exclude = ['garden']


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = '__all__'


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


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class CompanyPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.CharField(max_length=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'CompanyPermission'
        managed = True


class CompanyPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPermission
        fields = '__all__'


class GardenPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.CharField(max_length=1)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'restapi'
        db_table = 'GardenPermission'
        managed = True


class GardenPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenPermission
        fields = '__all__'
