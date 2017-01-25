# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 00:31
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

def set_default_openstack_settings(apps, schema_editor):
    """
    Update any instances with empty openstack_server_* fields using the current default settings.
    Note that any new instances created after this change will already have their openstack_server_* fields set.
    """
    OpenEdXInstance = apps.get_model("instance", "OpenEdXInstance")
    for instance in OpenEdXInstance.objects.all():
        if not instance.openstack_server_flavor:
            instance.openstack_server_flavor = settings.OPENSTACK_SANDBOX_FLAVOR
        if not instance.openstack_server_base_image:
            instance.openstack_server_base_image = settings.OPENSTACK_SANDBOX_BASE_IMAGE
        if not instance.openstack_server_ssh_keyname:
            instance.openstack_server_ssh_keyname = settings.OPENSTACK_SANDBOX_SSH_KEYNAME
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0072_openstack_settings'),
    ]

    operations = [
        migrations.RunPython(set_default_openstack_settings),
    ]
