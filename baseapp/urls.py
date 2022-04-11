from unicodedata import name
from django.urls import path
from baseapp.views import *

urlpatterns = [
    path('',home,name='landingpage'),
    path('home',myhome,name='homepage'),
    path('services',services, name='service'),
    path('our-work',ourWork,name='ourwork'),
    path('contact',contact,name='contact'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('new-born',newBorn,name='newborn'),
    path('infant',infant,name='infant'),
    path('materninty',materninty,name='materninty'),
    path('fashion',fashion,name='fashion'),
    path('send-data',formData,name='contactform'),
]
