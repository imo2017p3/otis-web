# Generated by Django 3.1.8 on 2021-06-04 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '0013_auto_20210603_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='group',
        ),
    ]
