# Generated by Django 3.2.5 on 2021-08-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_achievementcode_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementcode',
            name='diamonds',
            field=models.PositiveSmallIntegerField(
                default=1, help_text='Amount of diamonds for this achievement'),
        ),
        migrations.AddField(
            model_name='psetsubmission',
            name='eligible',
            field=models.BooleanField(
                default=True, help_text='Whether to count this for leveling up'),
        ),
    ]
