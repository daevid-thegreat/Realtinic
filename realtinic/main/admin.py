from django.contrib import admin
from .models import Agency, Property, Userprofile

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Property)
admin.site.register(Agency)