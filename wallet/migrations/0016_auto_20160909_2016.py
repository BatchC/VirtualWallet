# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 14:46
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0015_auto_20160908_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 9, 14, 46, 20, 570424, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debit',
            name='cvv',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 3 digits allowed.', regex='^\\+?1?\\d{3}$')]),
        ),
        migrations.AlterField(
            model_name='debit',
            name='debitNumber',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 12 digits allowed.', regex='^\\+?1?\\d{12}$')]),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 10 digits allowed.', regex='^\\+?1?\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='recharge',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 10 digits allowed.', regex='^\\+?1?\\d{10}$')]),
        ),
    ]
