# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 05:10
from __future__ import unicode_literals

from django.db import migrations, models


def populate_is_active(apps, schema_editor):
    '''
    Mark all OpenEdXInstance.active_appserver with OpenEdXAppServer.is_active = True
    '''

    OpenEdXInstance = apps.get_model("instance", "OpenEdXInstance")
    for instance in OpenEdXInstance.objects.exclude(active_appserver__isnull=True):
        active_appserver = instance.active_appserver
        # Set the underlying _is_active field; don't use the property setter.
        active_appserver._is_active = True
        active_appserver.save()


def populate_active_appserver(apps, schema_editor):
    '''
    Reverse populate_is active by setting OpenEdXInstance.active_appserver where OpenEdXAppServer.is_active = True

    WARNING: Can only keep the most recently activated appserver active, so multi-vms are not preserved.
    '''

    OpenEdXAppServer = apps.get_model("instance", "OpenEdXAppServer")
    OpenEdXInstance = apps.get_model("instance", "OpenEdXInstance")
    for appserver in OpenEdXAppServer.objects.filter(_is_active=True).order_by('owner_id', 'last_activated'):
        instance = OpenEdXInstance.objects.get(id=appserver.owner.instance_id)
        instance.active_appserver = appserver
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0076_auto_20170216_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='openedxappserver',
            name='_is_active',
            field=models.BooleanField(db_column='is_active', default=False),
        ),
        # ref http://stackoverflow.com/a/39541048/4302112
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE', reverse_sql=migrations.RunSQL.noop),
        migrations.RunPython(populate_is_active, populate_active_appserver),
        migrations.RunSQL(migrations.RunSQL.noop, reverse_sql='SET CONSTRAINTS ALL IMMEDIATE'),
        migrations.RemoveField(
            model_name='openedxinstance',
            name='active_appserver',
        ),
    ]
