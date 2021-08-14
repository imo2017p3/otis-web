# Generated by Django 3.2.5 on 2021-08-04 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_semester_uses_legacy_pset_system'),
        ('dashboard', '0027_rename_psetsubmission_pset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pset',
            name='next_unit_to_unlock',
            field=models.ForeignKey(blank=True, help_text='The unit you want to work on next (leave blank for any)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unblocking_psets', to='core.unit'),
        ),
    ]