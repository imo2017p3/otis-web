# Generated by Django 3.2.11 on 2022-02-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0070_auto_20220124_1249"),
    ]

    operations = [
        migrations.AddField(
            model_name="pset",
            name="rejected",
            field=models.BooleanField(
                default=False,
                help_text="If a problem set is rejected and needs attention.",
            ),
        ),
    ]
