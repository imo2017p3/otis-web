# Generated by Django 2.1.7 on 2019-03-28 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0023_auto_20190322_0810"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="assistant",
            field=models.ForeignKey(
                blank=True,
                help_text="The assistant for this student, if any",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="roster.Assistant",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="pointer_current_unit",
            field=models.ForeignKey(
                blank=True,
                help_text="If set, the counter will skip ahead so that the student is working on this unit instead.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pointer_unit",
                to="core.Unit",
            ),
        ),
    ]
