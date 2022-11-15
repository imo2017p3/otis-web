# Generated by Django 3.2.8 on 2021-10-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0006_alter_guess_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guess',
            options={'verbose_name_plural': 'Guesses'},
        ),
        migrations.AlterField(
            model_name='market',
            name='alpha',
            field=models.FloatField(
                default=2,
                help_text=
                'Exponent corresponding to harshness of the market, used in the scoring function'
            ),
        ),
    ]
