from django.shortcuts import redirect, render
from django.template import loader
import logging
from django.views.decorators.cache import cache_control
######################
from .forms import NewUserForm
from django.contrib import messages
from django.http import HttpResponse, response
from .models import User
from django.contrib.auth.hashers import make_password,check_password,is_password_usable

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
logging.debug('start')






@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_page(request):
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username and password:
        return render(request,'login.html')
    request.session[username] = username
    print(request.session)
    user_check = User.objects.filter(user_id=username)
    pass_db = user_check.values('password')[0]['password']
    if not user_check:
        return HttpResponse('No such user exist')
    else:
        if is_password_usable(pass_db):
            if check_password(password,pass_db):
                if username in request.session:
                    print(request.session[username])
                return render(request,"home.html")
            else:
                return HttpResponse('Enter correct  password')    
        if not user_check:
            return HttpResponse('Enter correct  user')

def register(request):
    return render(request, 'register.html')

def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    # User.objects.create(user_id=username.strip(),password=make_password(password.strip()))
    return render(request,"added.html",{"user":username})
