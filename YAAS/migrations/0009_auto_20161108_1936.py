# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 19:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YAAS', '0008_auto_20161107_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, default=1.0, help_text='The amount you want to raise the bid with', max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 19, 36, 53, 23817, tzinfo=utc), help_text='Enter the date like: YYYY-MM-DD HH:MM'),
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAAS.Auction'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
