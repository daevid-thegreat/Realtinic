# Generated by Django 3.2.13 on 2022-07-27 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220727_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='comment',
        ),
    ]