# Generated by Django 3.2.8 on 2021-10-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0002_market_alpha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='public',
            field=models.BooleanField(
                default=False,
                help_text=
                'If checked, will display your name next to your guess in the statistics, for bragging rights. By default, this is off and your guess is recorded anonymously.'
            ),
        ),
    ]
