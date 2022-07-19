from django.contrib import admin
from .models import Property, Userprofile, review, PropertyImage

class PropertyImageInline(admin.StackedInline):
    model = PropertyImage

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Property, PropertyAdmin)
admin.site.register(review)
admin.site.register(PropertyImage)