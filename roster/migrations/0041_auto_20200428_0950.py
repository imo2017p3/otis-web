# Generated by Django 3.0.3 on 2020-04-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0040_auto_20200428_0914"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitinquiry",
            name="action_type",
            field=models.CharField(
                choices=[
                    ("UNLOCK", "Unlock unit now"),
                    ("APPEND", "Add unit for later"),
                    ("DROP", "Drop unit"),
                ],
                help_text="Describe the action you want to make.",
                max_length=10,
            ),
        ),
    ]
