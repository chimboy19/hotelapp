from django.shortcuts import render,redirect
from rooms.models import Rooms
def Home (request):
    rooms=Rooms.objects.all().filter(is_avaliable=True )
    context={
      'rooms': rooms 
    }
    return render (request,'index.html',context)
    