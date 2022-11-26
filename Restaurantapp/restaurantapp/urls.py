from pydoc import visiblename
from django.contrib import admin
from django.urls import path,include
from restaurantapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
    path('response',views.response,name='response'),
    path('register',views.register,name='register'),
]