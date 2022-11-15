# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-05 14:03
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0012_student_legit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name='ID')),
                ('preps_taught',
                    models.SmallIntegerField(
                        default=0,
                        help_text=
                        'Number of semesters that development/preparation costs are charged.')),
                ('hours_taught',
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        help_text='Number of hours taught for.',
                        max_digits=8)),
                ('amount_owed',
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        help_text='Amount currently owed.',
                        max_digits=8)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student',
                    models.OneToOneField(
                        help_text='The invoice that this student is for.',
                        on_delete=django.db.models.deletion.CASCADE,
                        to='roster.Student')),
            ],
        ),
    ]
