# Generated by Django 3.2 on 2022-05-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0009_auto_20200302_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytranslation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
