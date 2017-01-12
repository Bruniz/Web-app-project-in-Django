# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 12:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('YAAS', '0028_auto_20161109_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 12, 25, 48, 451722, tzinfo=utc), help_text='Enter the date like: YYYY-MM-DD HH:MM'),
        ),
    ]
