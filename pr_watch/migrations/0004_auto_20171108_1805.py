# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-08 18:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations

import environ

class Migration(migrations.Migration):

    def create_watchedforks(apps, schema_editor):

        env = environ.Env()

        WatchedPullRequest = apps.get_model('pr_watch', 'WatchedPullRequest')
        WatchedFork = apps.get_model('pr_watch', 'WatchedFork')

        if WatchedPullRequest.objects.count() == 0:
            # This Ocim instance isn't used yet to watch PRs, so we should keep that feature disabled, therefore
            # we don't create any fork to watch
            return

        # To make all PR keep working, we try to use the old "watched fork name" and "watched organization" defined in
        # the .env file if they are still there (this will be the case when migrating instances which had PRs watcher).
        # After WATCH_FORK and WATCH_ORGANIZATION are removed from .env, we fall back to other sensible defaults
        fork_name = env("WATCH_FORK", default=getattr(settings, 'DEFAULT_FORK', None) or 'edx/edx-platform')
        organization = env("WATCH_ORGANIZATION", default=getattr(settings, 'DEFAULT_ADMIN_ORGANIZATION', None) or 'edx')
        default_fork = WatchedFork.objects.create(
            enabled=True,
            fork=fork_name,
            organization=organization,
        )
        for pr in WatchedPullRequest.objects.all():
            pr.watched_fork = default_fork
            pr.save()

    def delete_watchedforks(apps, schema_editor):
        WatchedPullRequest = apps.get_model('pr_watch', 'WatchedPullRequest')
        WatchedFork = apps.get_model('pr_watch', 'WatchedFork')
        for pr in WatchedPullRequest.objects.all():
            pr.watched_fork = None
            pr.save()
        WatchedFork.objects.all().delete()

    dependencies = [
        ('pr_watch', '0003_auto_20171108_1755'),
    ]

    operations = [
        migrations.RunPython(create_watchedforks, delete_watchedforks),
    ]
