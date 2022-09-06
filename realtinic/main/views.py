from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import *
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Sum, Q
import cloudinary.api
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
            if user.is_realtor == True:
                return redirect('/my-dashboard')
            else:
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
    # save property
    if request.user.is_authenticated:
        if request.method == 'POST' and 'save' in request.POST:
            property_id = request.POST['property_id']
            property = Property.objects.get(id=property_id)
            property.save()
            return redirect('index')

    properties = Property.objects.order_by('-listed_on')[:6]
    return render(request, 'index.html', {'properties':properties})

def listing(request):
    properties = Property.objects.all()
    search =  request.GET.get('keyword')
    query = request.GET.get('query')
    list_type =  request.GET.get('list_type')
    city =  request.GET.get('city')
    home_type = request.GET.get('home_type')
    price_range = request.GET.get('price-range2')
    area_range = request.GET.get('area-range2')
    bedrooms = request.GET.get('bedrooms')
    pool = request.GET.get('pool')
    garage = request.GET.get('garage')
    basement = request.GET.get('basement')

    context = {}

    if search:
        properties = properties.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )
        context['search'] = search
    if query:
        properties = properties.filter(location__icontains=query)
    if list_type:
        properties = properties.filter(list_type__icontains=list_type)
    if city:
        properties = properties.filter(city__icontains=city)
    if home_type:
        properties = properties.filter(home_type__icontains=home_type)
    if price_range:
        price_range = price_range.split(';')
        properties = properties.filter(
            Q(price__gte=price_range[0]) &
            Q(price__lte=price_range[1])
        )
    if area_range:
        area_range = area_range.split(';')
        properties = properties.filter(
            Q(yard_size__gte=area_range[0]) &
            Q(yard_size__lte=area_range[1])
        )
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)

    page = request.GET.get('page')
    props = Paginator(properties.order_by('-listed_on'), 12).get_page(page)
    nums = "p" * props.paginator.num_pages

    context = {
        "propertys": props,
        "nums" : nums
    }

    return render(request, 'listing.html', context)

def assign_features(value):
    features = ['pool', 'power', 'temp', 'garden', 'solar_power', 'drain', 'cctv', 'water']
    features_dict = {}
    for feature in features:
        if value[feature]: features_dict[feature] = 'yes'
        else: features_dict[feature] = 'no'
    
    return features_dict

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

            features = assign_features({
                'pool': pool,
                'power': power,
                'temp': temp,
                'garden': garden,
                'solar_power': solar_power,
                'drain': drain,
                'cctv': cctv,
                'water': water,
            })

            lot_size = request.POST['lot_size']
            yard_size = request.POST['yard_size']
            # upload image
            header_image = request.FILES.get('header_image')
            images = request.FILES.getlist('property_images')

            # for image in images:
            #     Property.objects.create(
            #         prop = Property, images = image)
            #     Property.save()
            

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

                pool=features['pool'],
                power=features['power'],
                temp=features['temp'],
                garden=features['garden'],
                solar_power=features['solar_power'],
                drain=features['drain'],
                cctv=features['cctv'],
                water=features['water'],
                
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
                agent=agent,
            )
            new_property.save()

            for image in images:
                prop_img = PropertyImage.objects.create(
                    property = new_property, 
                    property_image = image
                )
                prop_img.save()
            

        return render(request, 'dashboard-add-listing.html')
    else:
        return render(request, 'index.html')

@login_required(login_url='/')
def editlisting(request, id):
    if request.user.is_realtor == True:
        listing = Property.objects.get(id = id)
        listing = get_object_or_404(Property, id=id)
        if listing in request.user.properties.all():
            if request.method == 'POST':
                listing.name = request.POST['name']
                listing.location = request.POST['location']
                listing.list_type = request.POST['list_type']
                listing.city = request.POST['city']
                listing.price= request.POST['price']
                listing.home_type = request.POST['home_type']
                listing.rooms = request.POST['rooms']
                listing.bedrooms = request.POST['bedrooms']
                listing.full_bathrooms = request.POST['full_bathrooms']
                listing.half_bathrooms = request.POST['half_bathrooms']
                listing.one_quarter_bathrooms = request.POST['one_quarter_bathrooms']
                listing.three_quarter_bathrooms = request.POST['three_quarter_bathrooms']
                listing.garage = request.POST['garage']
                listing.telephone = request.POST.get('telephone', False)

                pool = request.POST.get('pool', False)
                power = request.POST.get('power', False)
                temp = request.POST.get('temp', False)
                garden = request.POST.get('garden', False)
                solar_power = request.POST.get('solar_power', False)
                drain = request.POST.get('drain', False)
                cctv = request.POST.get('cctv', False)
                water = request.POST.get('water', False)

                features = assign_features({
                    'pool': pool,
                    'power': power,
                    'temp': temp,
                    'garden': garden,
                    'solar_power': solar_power,
                    'drain': drain,
                    'cctv': cctv,
                    'water': water,
                })
                
                listing.pool = features['pool']
                listing.power = features['power']
                listing.temp = features['temp']
                listing.garden = features['garden']
                listing.solar_power = features['solar_power']
                listing.drain = features['drain']
                listing.cctv = features['cctv']
                listing.water = features['water']

                listing.lot_size = request.POST['lot_size']
                listing.yard_size = request.POST['yard_size']
                
                header_image = request.FILES.get('header_image')
                if header_image:
                    cloudinary.api.delete_resources(listing.header_image)
                    listing.header_image = header_image

                images = request.FILES.getlist('property_images')
                if images:
                    for prop_image in listing.images.all():
                        cloudinary.api.delete_resources(prop_image.property_image)
                    listing.images.all().delete()

                for image in images:
                    prop_img = PropertyImage.objects.create(
                        property = listing, 
                        property_image = image
                    )
                    prop_img.save()
                

                listing.description = request.POST['description']
                listing.built_on = request.POST['built_on']
                listing.video_link = request.POST['video_link']
                
                listing.save()
                
                return redirect('Edit listing', id)            

        return render(request, 'dashboard-add-listing.html', {'listing': listing})
    else:
        return render(request, 'index.html')
 
@login_required(login_url='/')
def logout(request):
        auth.logout(request)
        return redirect('/')

def findagents(request):
    agents= Userprofile.objects.all().filter(is_realtor = True)
    q = Paginator(agents, 10)
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
    user1 = str(request.user.id_user)
    user2 = str(user.id_user)
    room = user1[0:13] + "-" + user2[0:13]

    if user.is_realtor == True:
        if not Room.objects.filter(room_name = room).exists():
            Room.objects.create(room_name=room, user1 = request.user, user2 = user)
        room = Room.objects.get(room_name=room)
        return render(request, 'agent-single.html', {'user':user, 'room':room})
    else:
        if not Room.objects.filter().exists(room_name = room):
            Room.objects.create(room_name=room, user2 = request.user, user1 = user2)
        room = Room.objects.get(room_name=room)
        return render(request, 'user_single.html', {'user':user, 'room':room})

def compare(request):
    return render(request, 'compare.html')

def message(request):

    if request.user.is_realtor == True:
        return render(request, 'dashboard-messages.html')
    else:
        return render(request, 'user-messages.html')

def chat(request, room_name):
    # if not Room.objects.filter(room_name=room_name).exists():
    #      Room.objects.create(room_name=room_name, user1=request.user, user2=listing.agent)
    user = Userprofile.objects.get(id_user=request.user.id_user)
    room = Room.objects.get(room_name=room_name)
    chat = []
    chats = Chat.objects.filter(room=room)

    if request.user != room.user1 and request.user != room.user2:
            return redirect('/my-messages')
    return render(request, 'chat.html', {'room_name':room_name, 'user':user, 'room':room, 'chats':chats})

@login_required(login_url='/')
def dashboard(request):
    propertys = Property.objects.filter(agent=request.user)
    count_list = propertys.count()

    count_views = Property.objects.filter(agent=request.user).aggregate(Sum('views'))
    if count_views['views__sum'] is None:
        count_views['views__sum'] = 0

    count_saved = Property.objects.filter(agent=request.user).aggregate(Sum('saved'))
    if count_saved['saved__sum'] is None:
        count_saved['saved__sum'] = 0

    return render(request, 'dashboard.html', {'list_count':count_list, 'views_count':count_views['views__sum'], 'saved_count':count_saved['saved__sum']})

@login_required(login_url='/')
def user_profile(request):
    if request.user.is_realtor == True:
        if request.method == 'POST' and 'info' in request.POST:
            user_id = request.user.id_user
            user = Userprofile.objects.get(id_user=user_id)

            user.profilepic = request.FILES.get('profile-image')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.tel = request.POST.get('tel')
            user.address = request.POST.get('address')
            user.website = request.POST.get('website')
            user.bio = request.POST.get('bio')
            
            user.save()
            return redirect('my-profile')

        if request.method == 'POST' and 'pword' in request.POST:
            user_id = request.user.id_user
            password1 = request.POST['password']
            password2 = request.POST['password2']
            if request.user.check_password(request.POST['main_password']):
                if password1 == password2:
                    user = User.objects.get(id_user = user_id)
                    user.set_password(password1)
                    user.save()
                    return redirect('my-profile')
                else:

                    return render(request, 'my-profile.html', {'error':'Passwords do not match or current password is incorrect'})

        if request.method == 'POST' and 'socials' in request.POST:
            user_id = request.user.id_user
            user = Userprofile.objects.get(id_user=user_id)
            user.facebook = request.POST['facebook']
            user.twitter = request.POST['twitter']
            user.instagram = request.POST['instagram']
            user.linkedin = request.POST['linkedin']
            user.whatsapp = request.POST['whatsapp']
            user.save()
            return redirect('my-profile')
        return render(request, 'dashboard-myprofile.html')
    else:
        return render(request, 'user-profile.html')

def single_listing(request, id):
    listing = get_object_or_404(Property, id=id)
    listing.views += 1
    listing.save()
    reviews = Review.objects.filter(listing_id=listing)

    if request.user.is_authenticated:
        a = str(request.user.id_user)
        b = str(listing.agent.id_user)

        room = a[0:13] + "-" + b[0:13]
    
        if request.method == 'POST' and 'save' in request.POST:
            if listing in request.user.saved_property.all():
                listing.saved.add(request.user)
            else: 
                listing.saved.remove(request.user)
            return redirect('/listing/'+str(listing.id))
        if request.method == 'POST' and 'booking' in request.POST:
            tour_type = request.POST['tour_type']
            tour_date = request.POST['datepicker-here']
            tour_time = request.POST['time']

            booking = Booking.objects.create(
                property = listing,
                property_agent = listing.agent,
                user = request.user,
                tour_type = tour_type,
                start_date = tour_date,
                time = tour_time,
            )
            booking.save()
            return redirect('/listing/'+str(listing.id))


        if request.method == 'POST' and 'review' in request.POST:
            listing.reviews.create(
                author=request.user,
                comment=request.POST['comment'],
                rating=request.POST['rating'],
            )
            return redirect('/listing/'+str(listing.id))

        if request.method == 'POST' and 'booking' in request.POST:
            tour_type = request.POST['tour_type']
            tour_date = request.POST['datepicker-here']
            tour_time = request.POST['time']

            booking = Booking.objects.create(
                property = listing,
                property_agent = listing.agent,
                user = request.user,
                tour_type = tour_type,
                start_date = tour_date,
                time = tour_time,
            )
            booking.save()
            return redirect('/listing/'+str(listing.id))
        if request.user.is_realtor:
            if not Room.objects.filter(room_name=room).exists():
                Room.objects.create(room_name=room, user1 = request.user, user2 = listing.agent)
            room = Room.objects.get(room_name=room)
        else:
            if not Room.objects.filter(room_name=room).exists():
                Room.objects.create(room_name=room, user1 = listing.agent, user2 = request.user)
            room = Room.objects.get(room_name=room)
            if request.user != room.user1 and request.user != room.user2:
                return redirect('/my-messages')
        return render(request, 'listing-single3.html', {'listing': listing,'room':room})
    else:
        return render(request, 'listing-single3.html', {'listing': listing, 'reviews': reviews})

def my_listings(request):
    listings = request.user.properties.all()
    q = Paginator(listings, 12)
    page = request.GET.get('page')
    listings = q.get_page(page)
    nums = "p" * listings.paginator.num_pages
    return render(request, 'dashboard-listing-table.html', {'listings': listings, 'nums': nums})

def reviews(request):
    reviews = request.user.reviews.all()
    q = Paginator(reviews, 12)
    page = request.GET.get('page')
    reviews = q.get_page(page)
    nums = "p" * reviews.paginator.num_pages
    return render(request, 'dashboard-review.html', {'reviews': reviews, 'nums': nums})

def bookings(request):
    bookings = Booking.objects.filter(property_agent=request.user)
    return render(request, 'dashboard-bookings.html', {'bookings':bookings})

def saved_homes(request):
    if request.user.is_authenticated:
        saved_properties = request.user.saved_property.all()
        q = Paginator(saved_properties, 12)
        page = request.GET.get('page')
        saved_properties = q.get_page(page)
        nums = "p" * saved_properties.paginator.num_pages
        return render(request, 'dashboard-saved-homes.html', {'saved_properties': saved_properties, 'nums': nums})
    else:
        return render(request, 'login.html')