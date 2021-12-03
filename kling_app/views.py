from django.shortcuts import redirect, render
from django.template import loader
import logging
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse, response
from .models import User
from django.contrib.auth.hashers import make_password, check_password, is_password_usable

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.debug('start')



import pdb

def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # pdb.set_trace()

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            print('i am here')
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request=request, template_name="registration/login.html")
