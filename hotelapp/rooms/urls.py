# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.rooms,name='rooms'), 
    path('room_details/<int:id>/',views.room_details,name='room_details'), 

    
] 
