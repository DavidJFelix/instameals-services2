# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instameals', '0004_apiuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]
