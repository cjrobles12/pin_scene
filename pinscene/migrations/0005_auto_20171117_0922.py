# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinscene', '0004_pin_played'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='location',
            field=models.CharField(max_length=360),
        ),
    ]
