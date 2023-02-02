# Generated by Django 3.2.5 on 2021-08-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0063_alter_student_achievements"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="vision",
        ),
        migrations.AddField(
            model_name="student",
            name="usemo_score",
            field=models.SmallIntegerField(
                blank=True, help_text="The USEMO score for this year", null=True
            ),
        ),
    ]
