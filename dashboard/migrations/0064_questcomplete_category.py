# Generated by Django 3.2.8 on 2021-10-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0063_alter_pset_next_unit_to_unlock'),
    ]

    operations = [
        migrations.AddField(
            model_name='questcomplete',
            name='category',
            field=models.CharField(
                choices=[('PR', 'Pull request'), ('BR', 'Bug report'), ('WK', 'Wiki bonus'),
                            ('MO', 'Mock exam'), ('MS', 'Miscellaneous')],
                default='MS',
                max_length=4),
        ),
    ]
