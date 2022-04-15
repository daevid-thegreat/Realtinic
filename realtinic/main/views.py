from multiprocessing import context
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
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        print(full_name)
        print(email)
        print(password)


        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect('listing')
        else:

            user = User.objects.create_user(full_name=full_name, email=email, username=email, password=password)
            user.save() 

            user_model = User.objects.get(username=email)
            new_profile = Userprofile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return render(request, 'add-listing')

    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Sorry we cannot find this user')
            return redirect('index')
    return render(request, 'index.html')


def listing(request):
    return render(request, 'listing.html')

#@login_required(login_url='agent-login.html')
def addlisting(request):
    # if request.method == 'POST':

    #     property_name = request.POST['property_name']
    #     property_location = request.POST['property_location']
    #     list_type = request.POST['list_type']
    #     price = request.POST['price']
    #     home_type = request.POST['home_type']
    #     bedrooms = request.POST['bedrooms']
    #     bathrooms = request.POST['bathrooms']
    #     garage = request.POST['garage']
    #     lot_size = request.POST['lot_size']
    #     images = request.POST['images']
    #     description = request.POST['description']
    #     built_on = request.POST['built_on']
    #     property_link = request.POST['property_link']
    #     property_name = request.POST['property_name']
    #     property_name = request.POST['property_name']
        

    #     new_property = Property()
    #     new_property.save()


    #     return HttpResponse('Your property has been listed')
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
