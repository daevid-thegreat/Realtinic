from django.contrib import admin
from .models import Property, Userprofile, review

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Property)
admin.site.register(review)