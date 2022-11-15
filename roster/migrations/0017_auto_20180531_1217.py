# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-31 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0016_auto_20180107_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('semester', '-legit', 'name')},
        ),
        migrations.AddField(
            model_name='student',
            name='classification',
            field=models.CharField(
                choices=[('A', 'Weekly'), ('B', 'Biweekly'), ('C', 'Correspondence'),
                            ('N', 'Not applicable')],
                default='B',
                max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='legit',
            field=models.BooleanField(
                default=True,
                help_text=
                'Whether this student is still active. Set to false for dummy accounts and the like. This will hide them from the master schedule, for example.'
            ),
        ),
    ]
