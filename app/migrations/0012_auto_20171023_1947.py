# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-23 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import lib.CommaSeparatedStringsField


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170713_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='note_field_options',
            field=lib.CommaSeparatedStringsField.CommaSeparatedStringsField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='registration',
            name='note',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
