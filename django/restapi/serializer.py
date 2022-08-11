from rest_framework import serializers
from restapi.models import (
    Bed,
    Company,
    CompanyPermission,
    Coordinate,
    Garden,
    GardenPermission,
)

from django.contrib.auth.models import User


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


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        exclude = ['garden']


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class CompanyPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPermission
        fields = '__all__'


class GardenPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenPermission
        fields = '__all__'
