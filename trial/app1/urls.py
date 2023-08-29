from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
   path('',views.index, name= 'app1'),
   path('about', views.about, name= 'about'),
   path('services', views.services, name= 'services')
]
