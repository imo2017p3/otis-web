# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-25 06:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0018_auto_20180531_1222"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="assistant",
            options={},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ("semester", "-legit", "track")},
        ),
        migrations.RemoveField(
            model_name="student",
            name="name",
        ),
        migrations.AlterField(
            model_name="assistant",
            name="user",
            field=models.OneToOneField(
                default=1,
                help_text="The Django Auth user attached to the Assistant.",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="student",
            name="assistant",
            field=models.ForeignKey(
                blank=True,
                help_text="The assistant for this student, if any",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="roster.Assistant",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="assistant",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="assistant",
            name="name",
        ),
        migrations.RemoveField(
            model_name="assistant",
            name="semester",
        ),
    ]
