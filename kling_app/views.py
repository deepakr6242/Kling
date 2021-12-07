from django.shortcuts import redirect, render
from django.template import loader
import logging
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse, response
from .models import User
from django.contrib.auth.forms import AuthenticationForm
import pdb

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.debug('start')


def register_request(request):
    form_errors=None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home.html")
        else:
            form_errors=form.errors
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form_original = RegisterForm()
    print(form_errors)
    return render (request=request, template_name="register.html",context = {'form':form_original,
                                                                             "form_errors":form_errors})



def login_app(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request=request, template_name="home.html",
                              context={"username": username})
            else:
                return HttpResponse(" Invalid credentials")
        else:
            return render(request=request, template_name="registration/login.html",
                          context={"invalid_login_message": 'Check Your username/password'})
