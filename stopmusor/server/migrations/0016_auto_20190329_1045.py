# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-29 07:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_auto_20190329_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='image',
            field=models.ImageField(default=b'image.jpeg', upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='mapobjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 7, 45, 32, 122190)),
        ),
    ]
