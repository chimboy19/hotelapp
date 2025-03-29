# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.rooms,name='rooms'), 
    path('room_details/<int:id>/',views.room_details,name='room_details'), 
    path ('book_room/<int:room_id>/',views.book_room,name="book_room"),
    path("payment/<int:booking_id>/",views. payment_page, name="payment_page"),
    path("payment/confirm/<int:booking_id>/" ,views. payment_confirm, name="payment_confirm"),
    path("booking-success/",views. booking_success, name="booking_success"),


    
] 
