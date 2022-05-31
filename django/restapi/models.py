from django.db import models


class Garden(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        app_label = 'restapi'
        db_table = 'Garden'
        managed = True

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gardens = models.ManyToManyField(Garden)

    class Meta:
        app_label = 'restapi'
        db_table = 'Company'
        managed = True

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    companies = models.ManyToManyField(Company)

    class Meta:
        app_label = 'restapi'
        db_table = 'User'
        managed = True

    def __str__(self):
        return self.name
