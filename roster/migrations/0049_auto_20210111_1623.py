# Generated by Django 3.0.7 on 2021-01-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0048_drop_ws_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.CharField(
                choices=[('A', 'Weekly'), ('B', 'Biweekly'), ('C', 'Corr.'), ('E', 'Ext.'),
                            ('G', 'Grad'), ('N', 'N.A.'), ('P', 'Phantom')],
                help_text='The track that the student is enrolled in for this semester.',
                max_length=5),
        ),
    ]
