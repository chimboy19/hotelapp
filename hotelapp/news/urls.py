from django.urls import path

from . import views

urlpatterns = [
    path('blog',views.blogs,name='blogs'), 
    path('blog_details/<int:id>/',views.blogs_details,name='blog_details')
    


   

   
    
] 