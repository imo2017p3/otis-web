# Generated by Django 3.0.7 on 2020-09-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200810_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='zoom_room_url',
            field=models.CharField(
                blank=True,
                help_text='The entry point for the Zoom meeting room.',
                max_length=128),
        ),
    ]
