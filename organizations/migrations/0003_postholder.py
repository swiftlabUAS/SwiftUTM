# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-22 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0002_auto_20180222_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Man', 'Manager'), ('PIC', 'Pilot in Command'), ('HOT', 'Head of Training')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
