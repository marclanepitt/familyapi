# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20171023_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
