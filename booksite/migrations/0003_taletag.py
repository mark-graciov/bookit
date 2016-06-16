# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksite', '0002_auto_20160616_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('label', models.CharField(max_length=300)),
                ('help', models.CharField(max_length=300)),
            ],
        ),
    ]
