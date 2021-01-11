# Generated by Django 3.0.7 on 2020-12-29 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0018_auto_20200908_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_source', models.CharField(help_text='The source of the problem, such as `TSTST 2020/3`.If in doubt on formatting, follow what is written on the handout.If the problem does not include a source, do your bestto write a two or three word description of the problemthat can be recognized, like `100 sleepy students` or `sloth blocking ruler`.', max_length=255)),
                ('keywords', models.CharField(default='', help_text='A list of keywords that a solver could look at to help them guess whether the hint is relevant or not. These are viewable immediately, so no spoilers here.', max_length=255)),
                ('numbers', models.PositiveIntegerField(help_text='A number from 0 to 100 used to indicate an ordering for the hints.Here a number 0 means a small nudge given to someone at the very start whereas 100 means a hint given to someone who was read all previous hints or is close to the end of the problem.Do your best to make up an extrapolation for everything in between. A good idea is to give a sequence of hints with nearby numbers, say 20/21/22, each of which elaborates on the previous hint.')),
                ('content', models.TextField(help_text='The content of the hint. LaTeX rendering is okay.')),
                ('group', models.ForeignKey(help_text='The unit to which this problem belongs.', on_delete=django.db.models.deletion.CASCADE, to='core.UnitGroup')),
            ],
        ),
    ]
