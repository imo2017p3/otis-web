# Generated by Django 4.1.7 on 2023-03-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suggestions", "0005_problemsuggestion_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="problemsuggestion",
            name="feedback",
            field=models.TextField(
                blank=True, help_text="Comments by Evan on this suggestion"
            ),
        ),
    ]