from rest_framework import serializers

from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=32, null=True)

    class Meta:
        app_label = 'restapi'
        db_table = 'User'
        managed = True

    def __str__(self):
        return self.name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


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
