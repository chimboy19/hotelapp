from django.shortcuts import get_object_or_404, render,redirect
from rooms.models import Rooms
from django.core.mail import send_mail
from django.http import HttpResponse
from django .conf import settings
from django.contrib import messages


def Home (request):
    rooms=Rooms.objects.all().filter(is_available=True , is_homepage=True )
    
    context={
      'rooms': rooms ,
     
    }
    return render (request,'index.html',context)
    



def About_us(request):
    return render(request,'about-us.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            full_message = f"From: {name} <{email}>\n\n{message}"
            subject = f"New Contact Form Submission from {name}"

            try:
                send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=email,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been submitted.')
            except Exception as e:
                messages.error(request, 'There was an error sending your message.')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'contact.html')