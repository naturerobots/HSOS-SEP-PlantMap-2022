# Generated by Django 4.0.1 on 2022-07-26 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_remove_garden_image_garden_image_path_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinate',
            name='image',
        ),
        migrations.AddField(
            model_name='coordinate',
            name='garden',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='garden_coordinates',
                to='restapi.garden',
            ),
            preserve_default=False,
        ),
    ]
