from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.login,name='login'), 
    path('register/',views.register,name='register'), 
    path('login/',views.login,name='logout'),




    path('activate/<uidb64>/<token>/',views.activate,name='activate'), 

   
    
] 