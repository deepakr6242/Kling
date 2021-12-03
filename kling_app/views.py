from django.shortcuts import redirect, render
from django.template import loader
import logging
from django.views.decorators.cache import cache_control

from .forms import NewUserForm
from django.contrib import messages
from django.http import HttpResponse, response
from .models import User
from django.contrib.auth.hashers import make_password, check_password, is_password_usable

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.debug('start')





