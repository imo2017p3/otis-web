# Generated by Django 3.2.5 on 2021-07-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0060_studentregistration_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationcontainer',
            name='allowed_tracks',
            field=models.CharField(
                blank=True,
                help_text='A comma separated list of allowed tracks students can register for',
                max_length=256),
        ),
    ]
