# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20161219_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_pic_one',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_pic_three',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_pic_two',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
