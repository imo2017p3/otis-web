# Generated by Django 3.2.5 on 2021-08-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_remove_semester_registration_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='uses_legacy_pset_system',
            field=models.BooleanField(
                default=True,
                help_text='Whether the pset uses the old system of upload checking'),
            preserve_default=False,
        ),
    ]
