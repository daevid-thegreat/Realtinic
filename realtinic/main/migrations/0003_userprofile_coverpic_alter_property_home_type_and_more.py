# Generated by Django 4.0.3 on 2022-05-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_bio_userprofile_business_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='coverpic',
            field=models.ImageField(null=True, upload_to='agents cover image'),
        ),
        migrations.AlterField(
            model_name='property',
            name='home_type',
            field=models.CharField(choices=[('Single-family', 'Single-family'), ('Semi-detached', 'Semi-detached'), ('Apartment', 'Apartment'), ('Townhomes', 'Townhomes'), ('Multi-family', 'Multi-family'), ('Mobile/Manufactured', 'Mobile/Manufactured'), ('Condo', 'Condo')], default='Single-family', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='list_type',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='listed_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_city',
            field=models.CharField(choices=[('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Osun', 'Osun'), ('Ibadan', 'Ibadan')], default='Abuja', max_length=25),
        ),
    ]
