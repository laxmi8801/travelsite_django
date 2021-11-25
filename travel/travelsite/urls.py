from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('login',views.login, name='login'),
    path('register', views.register, name='register'),
    path('index',views.index,name='index'),
    path('book_now',views.book_now,name='book_now'),
    path('upcoming',views.upcoming,name='upcoming'),
    path('remove/<id>/',views.remove,name='remove'),
    path('admin',views.admin,name='admin'),
    path('logout',views.logout,name='logout'),
    path('decline/<id>/',views.decline,name='decline'),
    
    ]