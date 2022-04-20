# Generated by Django 4.0.3 on 2022-04-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_property_air_con_property_attic_property_basement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_city',
            field=models.CharField(choices=[('AB', 'Abuja'), ('LG', 'Lagos'), ('OS', 'Osun'), ('IB', 'Ibadan')], default='AB', max_length=25),
        ),
        migrations.AddField(
            model_name='property',
            name='property_tel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='yard_size',
            field=models.IntegerField(default=0),
        ),
    ]
