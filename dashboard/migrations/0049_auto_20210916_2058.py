# Generated by Django 3.2.7 on 2021-09-17 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0048_auto_20210916_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='palaceentry',
            name='visible',
            field=models.BooleanField(
                default=True,
                help_text=
                'Uncheck this box to hide your entry altogether (you can change your mind later)'
            ),
        ),
        migrations.AlterField(
            model_name='palaceentry',
            name='display_name',
            field=models.CharField(
                help_text='How you would like your name to be displayed in the Ruby Palace.',
                max_length=128),
        ),
        migrations.AlterField(
            model_name='palaceentry',
            name='message',
            field=models.TextField(help_text='You can write a message here', max_length=1024),
        ),
    ]
