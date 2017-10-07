# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 07:22
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0067_remove_blank_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='openedxappserver',
            name='additional_security_groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, help_text="Optional: A list of extra OpenStack security group names to use for this instance's VMs. A typical use case is to grant this instance access to a private database server that is behind a firewall. (In the django admin, separate group names with a comma.)", size=None),
        ),
        migrations.AddField(
            model_name='openedxinstance',
            name='additional_security_groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, help_text="Optional: A list of extra OpenStack security group names to use for this instance's VMs. A typical use case is to grant this instance access to a private database server that is behind a firewall. (In the django admin, separate group names with a comma.)", size=None),
        ),
        migrations.AlterField(
            model_name='openedxappserver',
            name='lms_users',
            field=models.ManyToManyField(blank=True, help_text='Instance manager users that should be made staff users on the instance.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='openedxinstance',
            name='lms_users',
            field=models.ManyToManyField(blank=True, help_text='Instance manager users that should be made staff users on the instance.', to=settings.AUTH_USER_MODEL),
        ),
    ]