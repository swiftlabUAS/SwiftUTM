# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-03 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utm_messages', '0004_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='receiver',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]
