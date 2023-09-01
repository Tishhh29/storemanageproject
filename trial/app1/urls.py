from django.contrib import admin
from django.urls import path
from app1 import views

from . import views


urlpatterns = [
    path('',views.index, name= 'app1'),
    path('populate', views.populate_fake_data, name='populate'),
    path('about', views.about, name= 'about'),
    path('services', views.services, name= 'services')
]
