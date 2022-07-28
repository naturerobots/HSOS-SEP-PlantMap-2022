import os
from uuid import uuid4

from rest_framework import serializers

from django.contrib.auth.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'date_joined', 'last_login']
        # fields = '__all__'
        extra_kwargs = {
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


class Garden(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    image = models.ImageField(upload_to=path_and_rename('garden-images'), null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'Garden'
        managed = True

    def __str__(self):
        return self.name


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
