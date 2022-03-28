from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Userprofile


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect('index')
        else:
            user = User.objects.create_user(full_name=full_name, email=email, password=password)
            user.save() 

            user_model = User.objects.get(full_name=full_name)
            new_profile = Userprofile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('index.html')
    else:
        return render(request, 'index.html')