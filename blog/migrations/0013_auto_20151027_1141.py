# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-27 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151025_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
