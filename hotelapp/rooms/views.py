from django.shortcuts import render,redirect,get_object_or_404
from django .contrib.auth.decorators import login_required
from django.urls import reverse
from django .conf import settings
from django.db.models import Q
from .models import Rooms,Booking
from django.contrib import messages
from datetime import datetime
import requests
from dateutil import parser
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
import random
from .models import ReviewRating
from .forms import ReviewForm
import string
# Create your views here.


def rooms (request):
    rooms=Rooms.objects.all().filter(is_available=True )
    paginator=Paginator(rooms,3)
    page=request.GET.get('page')
    paged_rooms=paginator.get_page(page)
    context={
      'rooms': paged_rooms
    }
    return render(request,'rooms.html',context)




def room_details(request,id):
    
    single_room=Rooms.objects.get(id=id)
    reviews=ReviewRating.objects .filter(room_id=single_room.id)
    booked=Booking.objects.filter(room=single_room,status='confirmed')
   
    context={
        'single_room':single_room,
        'reviews':reviews,
        'booked' :booked
       
    }

    return render(request,'room-details.html',context)





@login_required(login_url='login')
def book_room(request, room_id):
    room = get_object_or_404(Rooms, id=room_id)

    if request.method == "POST":
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')

       
        check_in_date = parser.parse(check_in).date()  
        check_out_date = parser.parse(check_out).date()

      
        total_days = (check_out_date - check_in_date).days
        if total_days <= 0:
            messages.error(request, "Check-out date must be after check-in date.")
            return redirect("room_details", id=room.id)

        total_price = total_days * room.price_per_night

       
        existing_booking = Booking.objects.filter(
            Q(room=room) &
            (Q(check_in__lt=check_out_date) & Q(check_out__gt=check_in_date))
        ).exists()

        if existing_booking:
            messages.error(request, "This room is already booked for the selected dates.")
            return redirect("room_details", id=room.id)
        
        reference=generate_reference()

      
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            check_in=check_in_date,
            check_out=check_out_date,
            guests=int(guests),
            total_price=total_price,
            status="pending",
            reference=reference
        )

        messages.success(request, "Room booked successfully. Proceed to payment.")
        return redirect("payment_page", booking_id=booking.id)

    return render(request, "room-details.html", {"room": room})

def generate_reference():
    return 'HBOOK' + ''.join(random.choices(string.digits, k=10))

def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    reference = generate_reference()

    context = {
        "booking": booking,
        "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY, 
         "reference": reference,
    }
    return render(request, "payment_page.html", context)



def payment_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    paystack_secret_key = settings.PAYSTACK_SECRET_KEY
    reference = request.GET.get("reference")

    if not reference:
        messages.error(request, "Invalid payment reference.")
        return redirect("payment_page", booking_id=booking.id)

   
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {"Authorization": f"Bearer {paystack_secret_key}"}
    response = requests.get(url, headers=headers)
    response_data = response.json()

    if response_data.get("status") and response_data["data"]["status"] == "success":
        
        booking.status = "confirmed"
        booking.save()
        messages.success(request, "Payment successful! Your booking is confirmed.")
        return redirect("booking_success")  
    else:
        messages.error(request, "Payment verification failed. Please contact support.")
        return redirect("payment_page", booking_id=booking.id)
    
   
    


def booking_success(request):
    return render(request, "booking_success.html")






def submit_review(request,room_id):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            reviews=ReviewRating.objects.get(user__id=request.user.id,room__id=room_id)
            form=ReviewForm (request.POST,instance=reviews)
            form.save()
            messages.success(request,'Thank you your review has been updated')
            return redirect(url)

        except ReviewRating .DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.rating=form.cleaned_data['rating']
                data.review=form.cleaned_data['review']
                data.ip=request.META.get('REMOTE_ADDR')
                data.room_id=room_id
                data.user_id=request.user.id
                data.save()
                messages.success(request,'Thank you your review has been submitted')
                return redirect(url)
            

           
            


def search(request):
    
    if 'keyword' in request.GET:
        keyword = request.GET ['keyword']
        if keyword:
            rooms=Rooms.objects.order_by('is_available').filter(Q(room_type__icontains=keyword ) | Q(room_number__icontains=keyword))
            room_count=rooms.count()
       
            
    context={
        'rooms':rooms,
        'room_count': room_count
    }
    
    return render(request,'rooms.html',context)