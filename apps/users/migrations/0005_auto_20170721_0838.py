# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170721_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='major',
            field=models.ManyToManyField(to='common.Major'),
        ),
    ]