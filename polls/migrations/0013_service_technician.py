# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20161219_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='technician',
            field=models.TextField(blank=True),
        ),
    ]
