# Generated by Django 4.0.3 on 2022-05-16 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_userprofile_id_userprofile_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='id_user',
            new_name='id_profile',
        ),
    ]
