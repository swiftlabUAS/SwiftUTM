# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_reserveairspace_geom2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserveairspace',
            name='geom2',
        ),
    ]
