# Generated by Django 3.2 on 2022-04-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20200302_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='career_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='partnertranslation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
