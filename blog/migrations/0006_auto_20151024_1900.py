# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-24 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151024_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='no_of_posts',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
