# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-16 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20190316_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
