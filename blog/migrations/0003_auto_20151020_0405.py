# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-19 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_author_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='n_blogs',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
