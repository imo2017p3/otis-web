# Generated by Django 2.1.7 on 2019-03-28 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20181206_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='unit',
            field=models.ForeignKey(
                blank=True,
                help_text='The unit for which this file is associated',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='core.Unit'),
        ),
    ]
