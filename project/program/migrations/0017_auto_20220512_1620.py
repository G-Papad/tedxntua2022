# Generated by Django 3.2 on 2022-05-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0016_alter_activity_workshoplink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='workshopLink',
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='workshopLink',
            field=models.URLField(blank=True, null=True, verbose_name='Workshop ticket'),
        ),
    ]
