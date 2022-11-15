# Generated by Django 3.2.5 on 2021-08-06 05:17

from django.db import migrations, models
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0024_auto_20210806_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examattempt',
            name='guess1',
            field=models.CharField(
                max_length=36,
                validators=[exams.models.expr_validator],
                verbose_name='Problem 1 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess2',
            field=models.CharField(
                max_length=36,
                validators=[exams.models.expr_validator],
                verbose_name='Problem 2 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess3',
            field=models.CharField(
                max_length=36,
                validators=[exams.models.expr_validator],
                verbose_name='Problem 3 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess4',
            field=models.CharField(
                max_length=36,
                validators=[exams.models.expr_validator],
                verbose_name='Problem 4 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess5',
            field=models.CharField(
                max_length=36,
                validators=[exams.models.expr_validator],
                verbose_name='Problem 5 response'),
        ),
    ]
