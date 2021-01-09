from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('about', views.xnx, name='about'),
    path('regis', views.regi, name='regis'),
    path('', views.user_login, name='login'),
    path('us_login', views.us_login, name='us_login'),
    path('logout', views.logoutUsers, name='logout'),
    path('register', views.us_regis, name='register'),

 ]

