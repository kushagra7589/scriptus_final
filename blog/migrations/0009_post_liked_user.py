# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-25 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20151025_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]