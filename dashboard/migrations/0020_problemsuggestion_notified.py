# Generated by Django 3.1.8 on 2021-05-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20210130_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemsuggestion',
            name='notified',
            field=models.BooleanField(
                default=False, help_text="Whether student has received the staff's comments."),
        ),
    ]
