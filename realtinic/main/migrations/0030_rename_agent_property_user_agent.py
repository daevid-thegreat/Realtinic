# Generated by Django 4.0.3 on 2022-04-25 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_property_agent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='agent',
            new_name='user_agent',
        ),
    ]
