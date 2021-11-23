from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=7)
    password = models.CharField(max_length=30)


def create_user(user_id,password):#create new user now manually later has to be passed from login function fucntion debt
    '''takes the user name and password add them to user table'''
    if not User.objects.filter(user_id=user_id):
        User.objects.create(user_id=user_id,password=make_password(password))
        return(user_id,'added to db')
    else:
        return ('user already exists')

create_user('test','test123')