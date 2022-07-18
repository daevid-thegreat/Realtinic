# Generated by Django 4.0.3 on 2022-07-13 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_userprofile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_image',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(blank=True, default='/Untitled274_20220622164957-removebg-preview.png', null=True, upload_to='agents profile image'),
        ),
        migrations.CreateModel(
            name='Property_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='property_images')),
                ('prop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.property')),
            ],
        ),
    ]
