# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-19 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
    ]
