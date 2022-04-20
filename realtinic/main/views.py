from random import randint
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Userprofile, Property
import random


# Create your views here.
def index(request):
    if request.method == 'POST' and 'signup' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        print(first_name + last_name)
        print(email)
        print(password)


        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect('listing')
        else:

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)
            user.save() 

            user_model = User.objects.get(username=email)
            new_profile = Userprofile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return render(request, 'listing')

    if request.method == 'POST' and 'signin' in request.POST : 
         email = request.POST['email']
         password = request.POST['password']
         print('logged in')
         user = auth.authenticate(username=email, password=password)
         if user is not None:
            auth.login(request, user)
            return redirect('/add-listing')
         else:
            messages.info(request, 'Sorry we cannot find this user')
            return redirect('index')


    l_property = Property.objects.order_by('-listed_on')[:6]
    return render(request, 'index.html', {'l_property':l_property})




def listing(request):
    return render(request, 'listing.html')

#@login_required(login_url='agent-login.html')
def addlisting(request):
    if request.method == 'POST':
         property_name = request.POST['property_name']
         property_location = request.POST['property_location']
         list_type = request.POST['list_type']
         property_city = request.POST['property_city']
         price = request.POST['price']
         home_type = request.POST['home_type']
         bedrooms = request.POST['bedrooms']
         full_bathrooms = request.POST['full_bathrooms']
         half_bathrooms = request.POST['half_bathrooms']
         one_quarter_bathrooms = request.POST['one_quarter_bathrooms']
         three_quarter_bathrooms = request.POST['three_quarter_bathrooms']
         garage = request.POST['garage']
         wifi = request.POST.get('wifi', False)
         indoor_pool = request.POST.get('indoor_pool', False)
         security = request.POST.get('security', False)
         equiped_kitchen = request.POST.get('equiped_kitchen', False)
         air_con = request.POST.get('air_con', False)
         solar_power = request.POST.get('solar_power', False)
         fireplace = request.POST.get('fireplace', False)
         attic = request.POST.get('attic', False)
         property_tel = request.POST.get('property_tel', False)
         chandelier = request.POST.get('chandelier', False)
         dishwasher = request.POST.get('dishwasher', False)
         dryer = request.POST.get('dryer', False)
         freezer_fridge = request.POST.get('freezer_fridge', False)
         oven = request.POST.get('oven', False)
         washing_machine = request.POST.get('washing_machine', False)
         garbage_disposer = request.POST.get('garbage_disposer', False)
         smoke_detector = request.POST.get('smoke_detector', False)
         patio = request.POST.get('patio', False)
         bbq_area = request.POST.get('bbq_area', False)
         pool = request.POST.get('pool', False)
         porch = request.POST.get('porch', False)
         sprinkler = request.POST.get('sprinkler', False)
         spa = request.POST.get('spa', False)
         garden = request.POST.get('garden', False)
         fence = request.POST.get('fence', False)
         bball = request.POST.get('bball', False)
         gate = request.POST.get('gate', False)
         sport_arena = request.POST.get('sport_arena', False)
         fitness_arena = request.POST.get('fitness_arena', False)
         tennis_court = request.POST.get('tennis_court', False)
         parking = request.POST.get('parking', False)
         laundry_room = request.POST.get('laundry_room', False)
         dining_room = request.POST.get('dining_room', False)
         library = request.POST.get('library', False)
         office = request.POST.get('office', False)
         workshop = request.POST.get('workshop', False)
         closets = request.POST.get('closets', False)
         basement = request.POST.get('basement', False)
         lot_size = request.POST['lot_size']
         yard_size = request.POST['lot_size']
         images = request.FILES.getlist('images')
         description = request.POST['description']
         built_on = request.POST['built_on']
         video_link = request.POST['video_link']
        

         new_property = Property.objects.create(property_name=property_name, property_city=property_city, property_tel=property_tel, property_location=property_location, list_type=list_type, price=price, home_type=home_type, bedrooms=bedrooms, full_bathrooms=full_bathrooms, half_bathrooms=half_bathrooms, one_quarter_bathrooms=one_quarter_bathrooms, three_quarter_bathrooms=three_quarter_bathrooms, garage=garage, wifi=wifi, indoor_pool=indoor_pool, security=security, equiped_kitchen=equiped_kitchen, air_con=air_con, solar_power=solar_power, fireplace=fireplace, attic=attic, chandelier=chandelier, dishwasher=dishwasher, dryer=dryer, freezer_fridge=freezer_fridge, oven=oven, washing_machine=washing_machine, garbage_disposer=garbage_disposer, smoke_detector=smoke_detector, patio=patio, bbq_area=bbq_area, pool=pool, porch=porch, sprinkler=sprinkler, spa=spa, garden=garden, fence=fence, bball=bball, gate=gate, sport_arena=sport_arena, fitness_arena=fitness_arena, tennis_court=tennis_court, parking=parking, laundry_room=laundry_room,dining_room=dining_room, library=library, office=office, workshop=workshop, closets=closets,basement=basement, lot_size=lot_size, yard_size=yard_size, images=images, description=description, built_on=built_on, video_link=video_link)
         new_property.save()
         return render(request, 'index.html')

    return render(request, 'dashboard-add-listing.html')


def propmanage(request):
    return render(request, 'prop-management.html') 

def findagents(request):
    return render(request, 'agent-list.html')

def help(request):
    return render(request, 'help.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def download(request):
    return render(request, 'download.html')

def privacy_policy(request):
    return render(request, 'privacy.html')
