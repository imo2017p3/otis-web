# Generated by Django 4.1.4 on 2023-01-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0043_unitgroup_artwork_thumb_md_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="unitgroup",
            name="artist_name",
            field=models.CharField(
                blank=True,
                help_text="Name of the artist for the unit artwork.",
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name="unitgroup",
            name="artist_show",
            field=models.BooleanField(
                default=True, help_text="Whether the artist name should be visible"
            ),
        ),
    ]
