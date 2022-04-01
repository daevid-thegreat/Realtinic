from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    location = models.CharField(max_length=120, blank=True)


    def __str__(self):
        return self.user.username
        
'''''class property(models.Model):
    property_name = pass
    property_type = pass
    listing_price = pass
    property_category = pass
    property_keywords = pass
    property_address = pass
    property_city = pass
    property_contact_email = pass
    property_contact_tel = pass
    property_website = pass
    property_header_image = pass
    property_area = pass
    property_bedrooms = pass
    property_bathrooms = pass
    build_date = pass
    garage = pass
'''
