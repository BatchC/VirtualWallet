# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-08 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_auto_20160908_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='plan',
            field=models.IntegerField(choices=[(10, 'Topup Rs.10, Talktime:Rs. 7.73, Validity: NA'), (20, 'Topup Rs.20, Talktime:Rs. 15.47, Validity: NA'), (30, 'Topup Rs.30, Talktime:Rs. 23.2, Validity: NA'), (50, 'Topup Rs.50, Talktime:Rs. 40.67, Validity: NA'), (58, 'Full Talktime + 250MB 3G Data'), (101, 'Full Talktime + All Local calls @1p/s'), (150, 'Full Talktime + 100 local sms'), (19, '2G Data 100MB, Validity: 3 days'), (52, '2G Data 100MB, Validity: 7 days'), (93, '2G Data 500MB, Validity: 7 days'), (127, '2G Data 1GB, Validity: 21 days'), (222, '3G Data 1GB, Validity: 28 days'), (247, '3G Data 1GB + Rs.30 TT, Validity: 28 days')]),
        ),
    ]
