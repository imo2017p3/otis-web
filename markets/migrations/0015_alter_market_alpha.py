# Generated by Django 3.2.8 on 2021-11-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0014_alter_market_alpha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='alpha',
            field=models.FloatField(
                blank=True,
                default=2,
                help_text=
                'Exponent corresponding to harshness of the market, used in the scoring function; leave blank for special scoring.',
                null=True),
        ),
    ]
