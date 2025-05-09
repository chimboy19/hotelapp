from django.shortcuts import get_object_or_404, render,redirect
from rooms.models import Rooms



def Home (request):
    rooms=Rooms.objects.all().filter(is_available=True , is_homepage=True )
    
    context={
      'rooms': rooms ,
     
    }
    return render (request,'index.html',context)
    



def About_us(request):
    return render(request,'about-us.html')







