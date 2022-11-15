# Generated by Django 3.0.7 on 2021-01-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '0004_auto_20210121_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='keywords',
            field=models.CharField(
                blank=True,
                default='',
                help_text=
                "A comma-separated list of keywords that a solver could look at to help them guess whether the hint is relevant or not. These are viewable immediately, so no spoilers here. Examples are `getting started`, `solution set`,`converse direction`, `construction`, etc. Not all problems go well with keywords, so you can leave this blank if you can't think of anything useful to write.",
                max_length=255),
        ),
    ]
