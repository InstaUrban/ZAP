# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_auto_20151203_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/img_usr'),
        ),
    ]
