# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_seen_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
