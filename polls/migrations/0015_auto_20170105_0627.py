# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20170103_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='serial_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
