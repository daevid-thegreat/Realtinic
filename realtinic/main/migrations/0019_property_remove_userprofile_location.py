# Generated by Django 4.0.3 on 2022-04-10 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_delete_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_name', models.CharField(default='property name', max_length=500)),
                ('property_location', models.CharField(default='property location', max_length=500)),
                ('list_type', models.CharField(choices=[('FS', 'For Sale'), ('FR', 'For Rent')], default='For Sale', max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('home_type', models.CharField(choices=[('SH', 'Single-family'), ('SD', 'Semi-detached'), ('AP', 'Apartment'), ('TH', 'Townhomes'), ('MF', 'Multi-family'), ('MH', 'Mobile/Manufactured'), ('CO', 'Condo')], default='Single-family', max_length=50)),
                ('property_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bedrooms', models.IntegerField(default=0)),
                ('full_bathrooms', models.IntegerField(default=0)),
                ('half_bathrooms', models.IntegerField(default=0)),
                ('three_quarter_bathrooms', models.IntegerField(default=0)),
                ('one_quarter_bathrooms', models.IntegerField(default=0)),
                ('garage', models.IntegerField(default=0)),
                ('lot_size', models.IntegerField(default=0)),
                ('images', models.ImageField(upload_to='property_images')),
                ('description', models.TextField(max_length=1000)),
                ('built_on', models.DateTimeField(null=True)),
                ('listed_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('video_link', models.URLField(blank=True, max_length=350, null=b'I01\n')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]