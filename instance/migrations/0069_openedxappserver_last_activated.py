# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0068_security_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='openedxappserver',
            name='last_activated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
