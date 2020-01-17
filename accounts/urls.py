
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('login', views.show_login, name='show_login'),
    path('do-login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
