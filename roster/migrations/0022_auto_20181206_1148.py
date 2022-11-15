# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-06 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0021_auto_20180825_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.CharField(
                choices=[('A', 'Weekly'), ('B', 'Biweekly'), ('C', 'Correspondence'),
                            ('E', 'External'), ('N', 'Not applicable')],
                max_length=5),
        ),
    ]
