from django.contrib import admin
from .models import Agency, Agent, Property, Userprofile

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Property)
admin.site.register(Agent)
admin.site.register(Agency)