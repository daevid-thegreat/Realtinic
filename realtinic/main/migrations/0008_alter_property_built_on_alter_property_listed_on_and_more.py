# Generated by Django 4.0.3 on 2022-04-04 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_property_built_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='built_on',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='property',
            name='listed_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='open_house',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_location',
            field=models.CharField(default='e.g 19 Queens Ave, Encino', max_length=500),
        ),
    ]
