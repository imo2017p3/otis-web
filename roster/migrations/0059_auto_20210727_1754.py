# Generated by Django 3.2.5 on 2021-07-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0058_auto_20210727_1656"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentregistration",
            name="email",
        ),
        migrations.RemoveField(
            model_name="studentregistration",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="studentregistration",
            name="last_name",
        ),
        migrations.AlterField(
            model_name="studentregistration",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Prefer not to say"),
                    ("M", "Male"),
                    ("F", "Female"),
                    ("H", "Nonbinary"),
                    ("O", "Other"),
                ],
                default="",
                help_text="If you are comfortable answering, specify which gender you most closely identify with.",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="studentregistration",
            name="track",
            field=models.CharField(
                choices=[
                    ("C", "Correspondence"),
                    ("B", "Meeting with Evan"),
                    ("E", "Meeting with another instructor"),
                    ("N", "None of the above"),
                ],
                max_length=6,
            ),
        ),
    ]
