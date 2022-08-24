# Generated by Django 3.2.13 on 2022-08-24 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_realtor', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='upload_agent_image')),
                ('bio', models.CharField(blank=True, max_length=700, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('tel', models.BigIntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('whatsapp', models.IntegerField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=50, null=True)),
                ('in_business_since', models.DateTimeField(blank=True, null=True)),
                ('gov_id', models.FileField(blank=True, null=True, upload_to='government ids')),
                ('business_id', models.FileField(blank=True, null=True, upload_to='business ids')),
                ('utility_bills', models.FileField(blank=True, null=True, upload_to='utility bills')),
                ('verified', models.BooleanField(default=False)),
                ('password', models.CharField(editable=False, max_length=250)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('list_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], max_length=25)),
                ('city', models.CharField(choices=[('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Osun', 'Osun'), ('Ibadan', 'Ibadan')], default='Abuja', max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('home_type', models.CharField(choices=[('Single-family', 'Single-family'), ('Semi-detached', 'Semi-detached'), ('Apartment', 'Apartment'), ('Townhomes', 'Townhomes'), ('Multi-family', 'Multi-family'), ('Mobile/Manufactured', 'Mobile/Manufactured'), ('Condo', 'Condo')], default='Single-family', max_length=50)),
                ('property_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('rooms', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('full_bathrooms', models.IntegerField(default=0)),
                ('half_bathrooms', models.IntegerField(default=0)),
                ('three_quarter_bathrooms', models.IntegerField(default=0)),
                ('one_quarter_bathrooms', models.IntegerField(default=0)),
                ('telephone', models.BigIntegerField(default=0)),
                ('garage', models.IntegerField(default=0)),
                ('pool', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('power', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('temp', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('garden', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('solar_power', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('cctv', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('drain', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('water', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=25)),
                ('lot_size', models.IntegerField(default=0)),
                ('yard_size', models.IntegerField(default=0)),
                ('header_image', models.ImageField(upload_to=main.models.upload_header_image)),
                ('description', models.TextField(max_length=1000)),
                ('complete', models.BooleanField(default=False)),
                ('built_on', models.DateTimeField(null=True)),
                ('listed_on', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('video_link', models.URLField(blank=True, max_length=350, null=True)),
                ('views', models.IntegerField(blank=True, default=0, editable=False, null=True)),
                ('agent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
                ('saved', models.ManyToManyField(blank=True, related_name='saved_property', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.CharField(choices=[('Bad', 'Bad'), ('Fair', 'Fair'), ('Average', 'Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], default='Fair', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_image', models.ImageField(upload_to=main.models.upload_property_image)),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.property')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_type', models.CharField(default=None, max_length=50)),
                ('start_date', models.DateField(default=None)),
                ('time', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main.property')),
                ('property_agent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
