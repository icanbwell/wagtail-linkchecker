# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaillinkchecker', '0005_scan_scan_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanlink',
            name='invalid',
            field=models.BooleanField(default=False),
        ),
    ]