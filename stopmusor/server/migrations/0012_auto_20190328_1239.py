# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-28 09:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_auto_20190328_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapobjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 28, 9, 39, 4, 525558)),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=b'static'),
        ),
    ]
