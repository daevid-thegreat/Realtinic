from random import randint
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf.urls import handler404, handler500
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from .models import Userprofile, Property, review
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
import time
from django.urls import reverse
User = get_user_model()


# Create your views here.

def handler404(request, exception=None):
    return render(request, '404.html')

def handler500(request, exception=None):
    return render(request, '500.html')


def index(request):
    if request.method == 'POST' and 'signup' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']


        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect('/')
        else:

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)
            user = auth.authenticate(username=email, password=password)
            login(request, user)
            return redirect('/my-profile')

    if request.method == 'POST' and 'signin' in request.POST : 
         email = request.POST['email']
         password = request.POST['password']
         user = auth.authenticate(username=email, password=password)
         if user is not None:
            auth.login(request, user)
            return redirect('/my-profile')
         else:
            messages.info(request, 'Sorry we cannot find this user')
            return redirect('index')

    properties = Property.objects.order_by('-listed_on')[:6]
    return render(request, 'index.html', {'properties':properties})




def listing(request):

        if request.method == 'GET':
            search =  request.GET.get('search')
            list_type =  request.GET.get('list_type')
            city =  request.GET.get('city')
            if search:       
                propertys = Paginator(Property.objects.filter(name__icontains =search).order_by('-listed_on')
                |Property.objects.filter(description__icontains =search).order_by('-listed_on'), 2)
                page = request.GET.get('page')
                propertys = propertys.get_page(page)
                nums = "p" * propertys.paginator.num_pages
                return render(request,'listing.html',{"propertys":propertys, "nums": nums, 'search':search})
            else:
                p = Paginator(Property.objects.order_by('-listed_on'), 2)
                page = request.GET.get('page')
                propertys = p.get_page(page)
                nums = "p" * propertys.paginator.num_pages
                return render(request, 'listing.html', {"propertys":propertys, "nums": nums})
        p = Paginator(Property.objects.order_by('-listed_on'), 2)
        page = request.GET.get('page')
        propertys = p.get_page(page)
        nums = "p" * propertys.paginator.num_pages
        return render(request, 'listing.html', {"propertys":propertys, "nums": nums})


@login_required(login_url='/')
def addlisting(request):
    if request.user.is_realtor == True:
        if request.method == 'POST':

            name = request.POST['name']
            location = request.POST['location']
            list_type = request.POST['list_type']
            city = request.POST['city']
            price= request.POST['price']
            home_type = request.POST['home_type']
            rooms = request.POST['rooms']
            bedrooms = request.POST['bedrooms']
            full_bathrooms = request.POST['full_bathrooms']
            half_bathrooms = request.POST['half_bathrooms']
            one_quarter_bathrooms = request.POST['one_quarter_bathrooms']
            three_quarter_bathrooms = request.POST['three_quarter_bathrooms']
            garage = request.POST['garage']
            telephone = request.POST.get('telephone', False)
            
            pool = request.POST.get('pool', False)
            power = request.POST.get('power', False)
            temp = request.POST.get('temp', False)
            garden = request.POST.get('garden', False)
            solar_power = request.POST.get('solar_power', False)
            drain = request.POST.get('drain', False)
            cctv = request.POST.get('cctv', False)
            water = request.POST.get('water', False)

            lot_size = request.POST['lot_size']
            yard_size = request.POST['lot_size']
            header_image = request.FILES.getlist('header_image')

            description = request.POST['description']
            built_on = request.POST['built_on']
            video_link = request.POST['video_link']
            agent = request.user
            

            new_property = Property.objects.create(
                name=name, 
                city=city, 
                telephone=telephone, 
                location=location, 
                list_type=list_type, 
                price=price, 
                home_type=home_type, 
                rooms=rooms, 
                bedrooms=bedrooms,

                pool=pool,
                power=power,
                temp=temp,
                garden=garden,
                solar_power=solar_power,
                drain=drain,
                cctv=cctv,
                water=water,
                
                full_bathrooms=full_bathrooms, 
                half_bathrooms=half_bathrooms, 
                one_quarter_bathrooms=one_quarter_bathrooms, 
                three_quarter_bathrooms=three_quarter_bathrooms, 
                garage=garage, 
                lot_size=lot_size, 
                yard_size=yard_size, 
                header_image=header_image, 
                description=description, 
                built_on=built_on, 
                video_link=video_link, 
                agent=agent
            )
            new_property.save()
            

        return render(request, 'dashboard-add-listing.html')
    else:
        return render(request, 'index.html')
 
@login_required(login_url='/')
def logout(request):
        auth.logout(request)
        return redirect('/')

def findagents(request):
    agents= Userprofile.objects.all().filter(is_realtor = True)
    print(agents)
    q = Paginator(agents, 2)

    page = request.GET.get('page')
    agents = q.get_page(page)
    nums = "p" * agents.paginator.num_pages
    return render(request, 'agent-list.html', {'nums': nums, 'agents':agents})

def findagency(request):
    return render(request, 'agency-list.html')

def help(request):
    return render(request, 'help.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'blog-single.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def download(request):
    return render(request, 'download.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def signin(request):
    return render(request, 'signin.html')

def agency_single(request):

    return render(request, 'agency-single.html')

def agents(request,):
    return redirect(request, 'find-agents')


def register_agents(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        tel = request.POST['tel']

        user = User.objects.get(first_name=first_name, last_name=last_name, email=email)
        user.is_realtor = True
        user.tel = tel
        user.save()

        return redirect('my_profile')
    return render(request, 'register-agent.html')

def user_single(request, id):
    user = Userprofile.objects.get(id_user = id)
    return render(request, 'agent-single.html', {'user':user})

def compare(request):
    return render(request, 'compare.html')

def message(request):
    return render(request, 'dashboard-messages.html')

@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/')
def user_profile(request):
    if request.user.is_realtor == True:
        return render(request, 'dashboard-myprofile.html')
    else:
        return render(request, 'user-profile.html')

def single_listing(request, id):
    listing = Property.objects.get(id = id)
    listing.views=listing.views+1
    listing.save()
    if request.method == 'POST' and 'save' in request.POST:
        listing.saved.add(request.user)
        return redirect('/listing/'+str(listing.property_id))

    if request.method == 'POST' and 'review' in request.POST:
        author = request.user
        comment = request.POST['comment']
        rating = request.POST['rating']
        listing = listing

        reviews = review.objects.create(author=author, comment=comment, rating=rating, listing=listing)
        reviews.save()
        return redirect('/listing/'+str(listing.property_id))

    return render(request, 'listing-single3.html', {'listing': listing})

def my_listings(request):
    return render(request, 'dashboard-listing-table.html')

def reviews(request):
    return render(request, 'dashboard-review.html')

def bookings(request):
    return render(request, 'dashboard-bookings.html')