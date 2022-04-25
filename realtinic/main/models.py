from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tel = models.IntegerField(default=000000000)


    def __str__(self):
        return self.user.username

class Agency(models.Model):
    agency_name = models.CharField(max_length=250)
    agency_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    agency_bio = models.CharField(max_length=700)
    agency_displayname = models.CharField(max_length=150)
    agency_tel = models.IntegerField(default=000000000)
    agency_profilepic = models.ImageField(upload_to="agency profile image")
    agency_email = models.EmailField()
    agency_website = models.URLField()
    agency_address = models.CharField(max_length=500)
    agency_rating = models.DecimalField(max_digits=5, decimal_places=1)
    agency_whatsapp = models.IntegerField()
    agency_facebook =models.URLField()
    agency_instagram =models.URLField()
    agency_twitter =models.URLField()
    agency_linkedin =models.URLField()

    def __str__(self):
        return self.agency_displayname

    

class Agent(models.Model):

    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    agent_name = models.CharField(max_length=250)
    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    in_business_since = models.DateTimeField(null=True)
    agent_bio = models.CharField(max_length=700)
    agent_displayname = models.CharField(max_length=150)
    agent_tel = models.IntegerField(default=000000000)
    agent_profilepic = models.ImageField(upload_to="agent profile image")
    agent_email = models.EmailField()
    agent_website = models.URLField()
    agent_license = models.CharField(max_length=700)
    agent_address = models.CharField(max_length=500)
    agent_rating = models.DecimalField(max_digits=5, decimal_places=1)
    agent_whatsapp = models.IntegerField()
    agent_facebook =models.URLField()
    agent_instagram =models.URLField()
    agent_twitter =models.URLField()
    agent_linkedin =models.URLField()

    def __str__(self):
        return self.agent_displayname


        
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

    property_city = (
        ('AB', 'Abuja'),
        ('LG','Lagos'),
        ('OS','Osun'),
        ('IB','Ibadan'),
    )

    list_types = (
        ('FS', 'For Sale'),
        ('FR','For Rent'),
    )
    true_false = (
        ('yes', 'yes'),
        ('no','no'),
    )
    currency = (
        ('NGN', 'Naira'),
        ('USD','Dollar'),
    )


    property_name = models.CharField(max_length=500, default='property name')
    property_location = models.CharField(max_length=500, default='property location')
    list_type = models.CharField(max_length=25, choices=list_types, default= 'FS')
    property_city = models.CharField(max_length=25, choices=property_city, default= 'AB')
    price= models.DecimalField(max_digits=13, decimal_places=2)
    home_type = models.CharField(max_length=50, choices=home_types, default= 'Single-family')
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
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
    listed_on =models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    video_link = models.URLField(max_length=350, null=True, blank=True)




    def __str__(self):
        return self.property_name
    