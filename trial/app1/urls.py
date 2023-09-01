from django.contrib import admin
from django.urls import path
from app1 import views

from . import views


urlpatterns = [
    path('',views.index, name= 'app1'),
    path('populate', views.populate_fake_data, name='populate'),
    path('about', views.about, name= 'about'),
    path('services', views.services, name= 'services'),
    path('store_employee_info', views.store_employee_info, name='store_employee_info'), 
    path('populate_store', views.populate_store, name='populate_store'),
    path('store_list', views.store_list, name='store_list'),
]
