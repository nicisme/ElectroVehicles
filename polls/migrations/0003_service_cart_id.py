# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161207_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cart_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Cart'),
            preserve_default=False,
        ),
    ]
