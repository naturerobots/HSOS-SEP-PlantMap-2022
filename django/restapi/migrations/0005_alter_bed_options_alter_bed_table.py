# Generated by Django 4.0.1 on 2022-06-08 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_garden_image_user_email_alter_company_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bed',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='bed',
            table='Bed',
        ),
    ]
