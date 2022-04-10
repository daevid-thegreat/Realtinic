# Generated by Django 4.0.3 on 2022-04-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_property_home_type_alter_property_list_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_link',
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='property',
            name='home_type',
            field=models.CharField(choices=[('SH', 'Single-family'), ('SD', 'Semi-detached'), ('AP', 'Apartment'), ('TH', 'Townhomes'), ('MF', 'Multi-family'), ('MH', 'Mobile/Manufactured'), ('CO', 'Condo')], default='Single-family', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_location',
            field=models.CharField(default='property location', max_length=500),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_name',
            field=models.CharField(default='property name', max_length=500),
        ),
        migrations.AlterField(
            model_name='property',
            name='video_link',
            field=models.URLField(blank=True, max_length=350, null=b'I01\n'),
        ),
    ]
