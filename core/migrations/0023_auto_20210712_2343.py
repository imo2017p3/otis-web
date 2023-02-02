# Generated by Django 3.2.5 on 2021-07-13 03:43

from django.db import migrations, models


def set_slug(apps, scheme_editor):
    UnitGroup = apps.get_model("core", "UnitGroup")
    for ug in UnitGroup.objects.all():
        ug.slug = ug.name.lower().replace(" ", "")
        ug.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0022_auto_20210504_0951"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="unit",
            name="prob_url",
        ),
        migrations.RemoveField(
            model_name="unit",
            name="soln_url",
        ),
        migrations.AddField(
            model_name="unitgroup",
            name="slug",
            field=models.SlugField(
                default=None,
                help_text="The slug for the filename for this unit group",
                max_length=80,
                null=True,
            ),
        ),
        migrations.RunPython(
            code=set_slug,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
