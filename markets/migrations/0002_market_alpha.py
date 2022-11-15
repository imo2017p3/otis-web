# Generated by Django 3.2.8 on 2021-10-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='alpha',
            field=models.FloatField(
                default=2,
                help_text=
                'Exponent corresponding to harshness of the market,  used in the scoring function'
            ),
        ),
    ]
