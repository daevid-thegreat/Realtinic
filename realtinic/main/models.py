from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #avatar = models.ImageField()

    id_user = models.IntegerField()


    def __str__(self):
        return self.user.username
        
class Property(models.Model):
    home_types = (
        ('SH', 'Single-family'),
        ('SD','Semi-detached'),
        ('AP','Apartment'),
        ('TH','Townhomes'),
        ('MF','Multi-family'),
        ('MH','Mobile/Manufactured'),
        ('CO','Condo'),
    )

    list_types = (
        ('FS', 'For Sale'),
        ('FR','For Rent'),
    )


    property_name = models.CharField(max_length=500, default='property name')
    property_location = models.CharField(max_length=500, default='property location')
    list_type = models.CharField(max_length=25, choices=list_types, default= 'FS')
    price= models.DecimalField(max_digits=13, decimal_places=2)
    home_type = models.CharField(max_length=50, choices=home_types, default= 'Single-family')
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    bedrooms = models.IntegerField(default=0)
    full_bathrooms = models.IntegerField(default=0)
    half_bathrooms = models.IntegerField(default=0)
    three_quarter_bathrooms = models.IntegerField(default=0)
    one_quarter_bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    lot_size = models.IntegerField(default=0)
    images = models.ImageField(upload_to='property_images')
    description = models.TextField(max_length=1000)
    built_on = models.DateTimeField(null=True)
    listed_on =models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    video_link = models.URLField(max_length=350, null=TRUE, blank=True)




    def __str__(self):
        return self.property_location
    