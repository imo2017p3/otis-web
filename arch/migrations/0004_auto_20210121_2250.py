# Generated by Django 3.0.7 on 2021-01-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '0003_auto_20210121_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='keywords',
            field=models.CharField(
                blank=True,
                default='',
                help_text=
                'A comma-separated list of keywords that a solver could look at to help them guess whether the hint is relevant or not. These are viewable immediately, so no spoilers here.',
                max_length=255),
        ),
    ]
