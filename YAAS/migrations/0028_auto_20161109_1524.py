# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAAS', '0027_auto_20161109_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(help_text='Enter the date like: YYYY-MM-DD HH:MM'),
        ),
    ]