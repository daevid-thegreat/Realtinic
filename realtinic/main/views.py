from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Userprofile, Property, review, PropertyImage,Booking
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Sum, Q
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
                return redirect('/my_dashboard')
            else:
                return redirect('/my_profile')

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
    
    properties = Property.objects.all()
    search =  request.GET.get('keyword')
    query = request.GET.get('query')
    list_type =  request.GET.get('list_type')
    city =  request.GET.get('city')
    home_type = request.GET.get('home_type')
    price_range = request.GET.get('price-range2')
    area_range = request.GET.get('area-range2')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
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
    props = Paginator(properties.order_by('-listed_on'), 2).get_page(page)
    nums = "p" * props.paginator.num_pages

    context = {
        "propertys": props,
        "nums" : nums
    }

    return render(request, 'listing.html', context)


@login_required(login_url='/')
def addlisting(request):
    if request.user.is_realtor == True:
        if request.method == 'POST':

            # print(request.POST)

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
    if user.is_realtor == True:
        return render(request, 'agent-single.html', {'user':user})
    else:
        return render(request, 'user_single.html', {'user':user})

def compare(request):
    return render(request, 'compare.html')

def message(request):
    return render(request, 'dashboard-messages.html')

@login_required(login_url='/')
def dashboard(request):
    propertys = Property.objects.filter(agent=request.user)
    count_list = propertys.count()

    count_views = Property.objects.filter(agent=request.user).aggregate(Sum('views'))
    if count_views['views__sum'] is None:
        count_views = 0

    count_saved = Property.objects.filter(agent=request.user).aggregate(Sum('saved'))
    if count_saved['saved__sum'] is None:
        count_saved = 0

    return render(request, 'dashboard.html', {'list_count':count_list, 'views_count':count_views['views__sum'], 'saved_count':count_saved})


@login_required(login_url='/')
def user_profile(request):
    if request.user.is_realtor == True:
        if request.method == 'POST' and 'info':
            user_id = request.user.id_user
            image = request.FILES.get('image')
            if image != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.image = image
                user.save()
            first_name = request.POST.get('first_name')
            if first_name != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.first_name = first_name
                user.save()
            last_name = request.POST.get('last_name')
            if last_name != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.last_name = last_name
                user.save()
            email = request.POST.get('email')
            if email != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.email = email
                user.save()
            tel = request.POST.get('tel')
            if tel != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.tel = tel
                user.save()
            address = request.POST.get('address')
            if address != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.location = address
                user.save()
            website = request.POST.get('website')
            if website != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.website = website
                user.save()
            bio = request.POST.get('bio')
            if bio != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.bio = bio
                user.save()
            return redirect('my_profile')

        if request.method == 'POST' and 'password':
            user_id = request.user.id_user
            password1 = request.POST['password']
            password2 = request.POST['password2']
            if user.check_password(request.POST['main_password']):
                if password1 == password2:
                    user = User.objects.get(id_user = user_id)
                    user.set_password(password1)
                    user.save()
                    return redirect('my-profile')
                else:

                    return render(request, 'my-profile.html', {'error':'Passwords do not match or current password is incorrect'})

        if request.method == 'POST' and 'socials':

            user_id = request.user.id_user
            facebook = request.POST['facebook']
            if facebook != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.facebook = facebook
                user.save()
            twitter = request.POST['twitter']
            if twitter != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.twitter = twitter
                user.save()
            instagram = request.POST['instagram']
            if instagram != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.instagram = instagram
                user.save()
            linkedin = request.POST['linkedin']
            if linkedin != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.linkedin = linkedin
                user.save()
            whatsapp = request.POST['whatsapp']
            if whatsapp != '':
                user = Userprofile.objects.get(id_user=user_id)
                user.whatsapp = whatsapp
                user.save()
            return redirect('my-profile')
        return render(request, 'dashboard-myprofile.html')
    else:
        return render(request, 'user-profile.html')

def single_listing(request, id):
    listing = Property.objects.get(id = id)
    listing = get_object_or_404(Property, id=id)
    listing.views += 1
    listing.save()

    # reviews = listing.reviews.all()
    
    if request.method == 'POST' and 'save' in request.POST:
        if listing in request.user.saved_property.all():
            listing.saved.add(request.user)
            print('do')
        else: 
            listing.saved.remove(request.user)
        return redirect('/listing/'+str(listing.id))

    if request.method == 'POST' and 'booking' in request.POST:
        tour_type = request.POST['tour_type']
        tour_date = request.POST['datepicker-here']
        tour_time = request.POST['time']

        booking = Booking.objects.create(
            listing = listing,
            user = request.user,
            tour_type = tour_type,
            tour_date = tour_date,
            tour_time = tour_time,
        )
        print(booking)
        booking.save()
        return redirect('/listing/'+str(listing.id))


    if request.method == 'POST' and 'review' in request.POST:
        listing.reviews.create(
            author=request.user,
            comment=request.POST['comment'],
            rating=request.POST['rating'],
        )
        # author = request.user
        # comment = request.POST['comment']
        # rating = request.POST['rating']
        # listing = listing

        # reviews = review.objects.create(author=author, comment=comment, rating=rating, listing=listing)
        # reviews.save()
        return redirect('/listing/'+str(listing.id))

    return render(request, 'listing-single3.html', {'listing': listing})

def my_listings(request):
    return render(request, 'dashboard-listing-table.html')

def reviews(request):
    return render(request, 'dashboard-review.html')

def bookings(request):
    return render(request, 'dashboard-bookings.html')