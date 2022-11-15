# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:09
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20170806_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name='ID')),
                ('curriculum',
                    models.ManyToManyField(
                        help_text='The choice of units that this student will work on',
                        to='core.Unit')),
                ('semester',
                    models.ForeignKey(
                        help_text='The semester for this student',
                        on_delete=django.db.models.deletion.CASCADE,
                        to='core.Semester')),
                ('user',
                    models.ForeignKey(
                        help_text='The Django Auth user attached to the student',
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
