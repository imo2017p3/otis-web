# Generated by Django 2.1.11 on 2019-12-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0031_auto_20191201_1112"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="newborn",
            field=models.BooleanField(
                default=False, help_text="Whether the student is newly created."
            ),
            preserve_default=False,
        ),
    ]
