from email.policy import default
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from datetime import datetime

from realtinic.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL

class UserprofileManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password, **other_fields ):
        
        if not email:
            raise ValueError("you must add an email")

        email = self.normalize_email(email)
        user = self.model(first_name= first_name, last_name = last_name, username = username, email =email, password = password, **other_fields)
        user.set_password(password)
        user.save()

        return user.first_name

    def create_realtor(self, first_name, last_name, username, email, password, **other_fields ):
        user = self.create_user(first_name, last_name, username, email, password, **other_fields)
        user.is_realtor = True
        user.save()

        return user.first_name

    def create_superuser(self, first_name, last_name, username, email, password, **other_fields ):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned is_superuser=True')

        return self.create_user(first_name, last_name, username, email, password, **other_fields)


class Userprofile(AbstractBaseUser, PermissionsMixin):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    #saved properties - many to one

    profilepic = models.ImageField(upload_to="agents profile image", null=True, blank=True)
    coverpic = models.ImageField(upload_to="agents cover image", null=True, blank=True)
    bio = models.CharField(max_length=700, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    tel = models.BigIntegerField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    whatsapp = models.IntegerField(null=True, blank=True)
    facebook =models.URLField(null=True, blank=True)
    instagram =models.URLField(null=True, blank=True)
    twitter =models.URLField(null=True, blank=True)
    linkedin =models.URLField(null=True, blank=True)

    in_business_since = models.DateTimeField(null=True, blank=True)
    gov_id = models.FileField(upload_to='government ids', null=True, blank=True)
    business_id = models.FileField(upload_to='business ids', null=True, blank=True)
    utility_bills = models.FileField(upload_to='utility bills', null=True, blank=True)

    verified = models.BooleanField(default=False)

    password = models.CharField(max_length=250)
    objects = UserprofileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']



    def __str__(self):
        return self.username




# class Agency(models.Model):
#     agency_name = models.CharField(max_length=250)
#     agency_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     agency_bio = models.CharField(max_length=700)
#     agency_displayname = models.CharField(max_length=150)
#     agency_tel = models.IntegerField(default=000000000)
#     agency_profilepic = models.ImageField(upload_to="agency profile image")
#     agency_email = models.EmailField()
#     agency_website = models.URLField()
#     agency_address = models.CharField(max_length=500)
#     agency_rating = models.DecimalField(max_digits=5, decimal_places=1)
#     agency_whatsapp = models.IntegerField()
#     agency_facebook =models.URLField()
#     agency_instagram =models.URLField()
#     agency_twitter =models.URLField()
#     agency_linkedin =models.URLField()

#     def __str__(self):
#         return self.agency_displayname
        
class Property(models.Model):
    home_types = (
        ('Single-family', 'Single-family'),
        ('Semi-detached','Semi-detached'),
        ('Apartment','Apartment'),
        ('Townhomes','Townhomes'),
        ('Multi-family','Multi-family'),
        ('Mobile/Manufactured','Mobile/Manufactured'),
        ('Condo','Condo'),
    )

    property_city = (
        ('Abuja', 'Abuja'),
        ('Lagos','Lagos'),
        ('Osun','Osun'),
        ('Ibadan','Ibadan'),
    )

    list_types = (
        ('For Sale', 'For Sale'),
        ('For Rent','For Rent'),
    )
    true_false = (
        ('yes', 'yes'),
        ('no','no'),
    )
    currency = (
        ('Naira', 'Naira'),
        ('Dollar','Dollar'),
    )


    property_name = models.CharField(max_length=500, default='property name')
    property_location = models.CharField(max_length=500, default='property location')
    list_type = models.CharField(max_length=25, choices=list_types, default= 'For Sale')
    property_city = models.CharField(max_length=25, choices=property_city, default= 'Abuja')
    price= models.DecimalField(max_digits=13, decimal_places=2)
    home_type = models.CharField(max_length=50, choices=home_types, default= 'Single-family')
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    full_bathrooms = models.IntegerField(default=0)
    half_bathrooms = models.IntegerField(default=0)
    three_quarter_bathrooms = models.IntegerField(default=0)
    one_quarter_bathrooms = models.IntegerField(default=0)
    property_tel = models.BigIntegerField(default=000000000000)
    garage = models.IntegerField(default=0)
    wifi = models.CharField(max_length=25, choices=true_false, default= 'no')
    indoor_pool = models.CharField(max_length=25, choices=true_false, default= 'no')
    security = models.CharField(max_length=25, choices=true_false, default= 'no')
    equiped_kitchen = models.CharField(max_length=25, choices=true_false, default= 'no')
    air_con = models.CharField(max_length=25, choices=true_false, default= 'no')
    solar_power = models.CharField(max_length=25, choices=true_false, default= 'no')
    fireplace = models.CharField(max_length=25, choices=true_false, default= 'no')
    attic = models.CharField(max_length=25, choices=true_false, default= 'no')
    chandelier = models.CharField(max_length=25, choices=true_false, default= 'no')
    dishwasher = models.CharField(max_length=25, choices=true_false, default= 'no')
    dryer = models.CharField(max_length=25, choices=true_false, default= 'no')
    freezer_fridge = models.CharField(max_length=25, choices=true_false, default= 'no')
    oven = models.CharField(max_length=25, choices=true_false, default= 'no')
    washing_machine = models.CharField(max_length=25, choices=true_false, default= 'no')
    garbage_disposer = models.CharField(max_length=25, choices=true_false, default= 'no')
    smoke_detector = models.CharField(max_length=25, choices=true_false, default= 'no')
    patio = models.CharField(max_length=25, choices=true_false, default= 'no')
    bbq_area = models.CharField(max_length=25, choices=true_false, default= 'no')
    pool = models.CharField(max_length=25, choices=true_false, default= 'no')
    porch = models.CharField(max_length=25, choices=true_false, default= 'no')
    sprinkler = models.CharField(max_length=25, choices=true_false, default= 'no')
    spa = models.CharField(max_length=25, choices=true_false, default= 'no')
    garden = models.CharField(max_length=25, choices=true_false, default= 'no')
    user_agent = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    fence = models.CharField(max_length=25, choices=true_false, default= 'no')
    bball = models.CharField(max_length=25, choices=true_false, default= 'no')
    gate = models.CharField(max_length=25, choices=true_false, default= 'no')
    sport_arena = models.CharField(max_length=25, choices=true_false, default= 'no')
    fitness_arena = models.CharField(max_length=25, choices=true_false, default= 'no')
    tennis_court = models.CharField(max_length=25, choices=true_false, default= 'no')
    parking = models.CharField(max_length=25, choices=true_false, default= 'no')
    laundry_room = models.CharField(max_length=25, choices=true_false, default= 'no')
    dining_room = models.CharField(max_length=25, choices=true_false, default= 'no')
    library = models.CharField(max_length=25, choices=true_false, default= 'no')
    office = models.CharField(max_length=25, choices=true_false, default= 'no')
    workshop = models.CharField(max_length=25, choices=true_false, default= 'no')
    closets = models.CharField(max_length=25, choices=true_false, default= 'no')
    basement = models.CharField(max_length=25, choices=true_false, default= 'no')
    lot_size = models.IntegerField(default=0)
    yard_size = models.IntegerField(default=0)
    images = models.FileField(upload_to='property_images')
    description = models.TextField(max_length=1000)
    complete = models.BooleanField(default=False)
    built_on = models.DateTimeField(null=True)
    listed_on =models.DateTimeField(auto_now_add=False, auto_now=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    video_link = models.URLField(max_length=350, null=True, blank=True)




    def __str__(self):
        return self.property_name

    @property
    def total_bathrooms(self):
        total_bathrooms = self.full_bathrooms + self.half_bathrooms + self.three_quarter_bathrooms + self.one_quarter_bathrooms
        return total_bathrooms
    