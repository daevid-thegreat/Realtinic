# Generated by Django 3.2.13 on 2022-07-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='listing',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
