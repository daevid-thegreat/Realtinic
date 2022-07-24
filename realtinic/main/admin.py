from django.contrib import admin
from .models import Property, Userprofile, review, PropertyImage

class PropertyImageInline(admin.StackedInline):
    model = PropertyImage
    extra = 0

class UserPropertyInline(admin.StackedInline):
    model = Property
    fields = ['name']
    extra = 0 
    can_delete = False

class ReviewInline(admin.StackedInline):
    model = review
    fields = ['rating']
    extra = 0 
    can_delete = False

# Register your models here.
@admin.register(Userprofile)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'is_realtor',
        # 'properties__sum',
        'verified'
    ]
    inlines = [UserPropertyInline, ReviewInline]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'list_type',
        'city',
        'price',
        'home_type',
        'agent',
        'average_review'
    ]
    inlines = [PropertyImageInline, ReviewInline]

admin.site.register(review)
# admin.site.register(PropertyImage)