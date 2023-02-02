# Generated by Django 3.2.7 on 2021-09-26 16:58

from django.db import migrations, models

import dashboard.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0057_alter_achievement_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semesterdownloadfile",
            name="content",
            field=models.FileField(
                help_text="The file itself",
                upload_to=dashboard.models.download_file_name,
            ),
        ),
    ]
