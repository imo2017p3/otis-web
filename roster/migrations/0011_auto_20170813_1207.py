# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0010_auto_20170813_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assistant',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('name',)},
        ),
    ]
