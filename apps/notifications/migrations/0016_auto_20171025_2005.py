# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0015_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, to='notifications.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
