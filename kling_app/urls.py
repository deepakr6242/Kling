from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path(r'home/',views.home, name='home'),
    path(r'register/', views.register, name="register"),
    path(r"add_user/", views.add_user, name="add_user"),
    
]