# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-25 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20180123_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveairspace',
            name='application_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
