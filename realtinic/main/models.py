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
    location = models.CharField(max_length=120, blank=True)


    def __str__(self):
        return self.user.username
        
class Property(models.Model):
    home_types = (
        ('BG', 'Bungalow'),
        ('DP','Duplex'),
        ('AP','Apartment'),
        ('MN','Mansion'),
        ('VA','Villa'),
        ('CO','Condo'),
    )

    list_types = (
        ('FS', 'For Sale'),
        ('FR','For Rent'),
    )


    property_name = models.CharField(max_length=250, default='e.g 19 Queens Ave, Encino')
    property_location = models.CharField(max_length=250, default='e.g 19 Queens Ave, Encino')
    list_type = models.CharField(max_length=2, choices=list_types, default= 'For Sale')
    price= models.DecimalField(max_digits=13, decimal_places=2)
    home_type = models.CharField(max_length=2, choices=home_types, default= 'Bungalow')
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    property_price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    lot_size = models.IntegerField(default=0)
    images = models.ImageField(upload_to='property_images')
    description = models.TextField(max_length=600)
    built_on = models.DateTimeField(null=True)
    listed_on =models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    property_link = models.URLField(max_length=150, null=TRUE)



    def __str__(self):
        return self.property_location
    