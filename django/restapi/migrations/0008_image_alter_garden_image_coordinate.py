# Generated by Django 4.0.1 on 2022-07-25 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_alter_garden_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='garden',
            name='image',
            field=models.ImageField(null=True, upload_to='garden-images/d6830fdf5b484eeb987b1472bede01ab.png'),
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.image')),
            ],
        ),
    ]