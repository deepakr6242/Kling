from django.urls import path,include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    # path(r'home/',views.home, name='home'),
    # path(r'register/', views.register, name="register"),

    # path(r"add_user/", views.add_user, name="add_user"), 

    # path(r"add_user/", views.add_user, name="add_user"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    

]