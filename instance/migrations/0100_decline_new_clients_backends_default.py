# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-04 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0099_auto_20171103_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadbalancingserver',
            name='accepts_new_backends',
            field=models.BooleanField(default=False, help_text='Whether new backends can be assigned to this load-balancing server.'),
        ),
        migrations.AlterField(
            model_name='mongodbserver',
            name='accepts_new_clients',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mysqlserver',
            name='accepts_new_clients',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rabbitmqserver',
            name='accepts_new_clients',
            field=models.BooleanField(default=False),
        ),
    ]