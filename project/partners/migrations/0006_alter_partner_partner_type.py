<<<<<<< HEAD
# Generated by Django 3.2 on 2022-05-12 09:17
=======
# Generated by Django 3.2 on 2022-05-11 10:52
>>>>>>> 34e87411b0341d8ebfd4c28e7b2ee530bd5e6686

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_auto_20220428_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_type',
<<<<<<< HEAD
            field=models.CharField(choices=[('PS', 'Platinum Sponsor'), ('GS', 'Grand Sponsors'), ('GCS', 'Grand Carrier Sponsors'), ('GHS', 'Grand Hospitality Sponsors'), ('SPO', 'Sponsors'), ('SUP', 'Supporters'), ('MP', 'Media Partners'), ('CP', 'Community Partners'), ('KP', 'Knowledge Partners')], max_length=3),
=======
            field=models.CharField(choices=[('KP', 'Knowledge Partners'), ('PS', 'Platinum Sponsor'), ('GS', 'Grand Sponsors'), ('GCS', 'Grand Carrier Sponsors'), ('GHS', 'Grand Hospitality Sponsors'), ('SPO', 'Sponsors'), ('SUP', 'Supporters'), ('MP', 'Media Partners'), ('CP', 'Community Partners')], max_length=3),
>>>>>>> 34e87411b0341d8ebfd4c28e7b2ee530bd5e6686
        ),
    ]
