# Generated by Django 4.0.3 on 2022-05-20 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_userprofile_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.FileField(upload_to='property_header_images'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='property_images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.property')),
            ],
        ),
    ]
