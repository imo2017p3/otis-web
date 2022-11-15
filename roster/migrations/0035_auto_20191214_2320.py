# Generated by Django 2.1.15 on 2019-12-15 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0034_auto_20191213_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.CharField(
                choices=[('A', 'Weekly'), ('B', 'Biweekly'), ('BW', 'Biwk. WS'), ('C', 'Corr.'),
                            ('CW', 'Corr. WS'), ('E', 'Ext.'), ('G', 'Grad'), ('N', 'N.A.')],
                help_text='The track that the student is enrolled in for this semester.',
                max_length=5),
        ),
    ]
