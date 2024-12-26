from django.shortcuts import render,redirect
from .models import Rooms
# Create your views here.


def rooms (request):
    rooms=Rooms.objects.all().filter(is_avaliable=True )
    context={
      'rooms': rooms 
    }
    return render(request,'rooms.html',context)




def room_details(request,id):
    
    single_room=Rooms.objects.get(id=id)
    context={
        'single_room':single_room
    }

    return render(request,'room-details.html',context)