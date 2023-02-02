# Generated by Django 4.0.8 on 2022-12-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0041_unitgroup_artwork"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitgroup",
            name="subject",
            field=models.CharField(
                choices=[
                    ("A", "Algebra (Hufflepuff)"),
                    ("C", "Combinatorics (Gryffindor)"),
                    ("G", "Geometry (Slytherin)"),
                    ("N", "Number Theory (Ravenclaw)"),
                    ("F", "Functional Equations"),
                    ("M", "Miscellaneous"),
                    ("K", "Secret"),
                ],
                help_text="The subject for the unit",
                max_length=2,
            ),
        ),
    ]
