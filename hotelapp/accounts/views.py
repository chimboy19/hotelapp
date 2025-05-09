from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages,auth
from django .contrib.auth.decorators import login_required
from .models import Account
from rooms .models import Booking
# email verification 
from django .contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# import requests


# Create your views here.







def register (request):
    if request .method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            username=email.split('@')[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.save()

    
         # User Activation
            current_site= get_current_site(request)
            mail_subject='please activate your account'
            message=render_to_string('account/account_verification_email.html',{
            'user': user,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject, message ,to=[to_email])
            send_email.send()
            # messages.success(request,'Registration successful')
            return redirect('/accounts/login/?command=verification&email='+email)
        
    else:
        form=RegistrationForm()
    context={
        'form' :form
    }
    return render(request,'account/registration.html',context)






def login (request):
    if request.method=='POST':
        email = request.POST['email'] # ✅ Correct way
        password = request.POST['password']
        user=auth.authenticate(email=email,password=password)
        print(f"Authenticated User: {user}")

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'you have succesfully logged in')
            return redirect('Home')
        else:
            messages.error(request,'invaid login credentails')
            return redirect('login')

    return render(request,'account/login.html')



def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'congratulations your account is activated' )
        return redirect('login')
    else :
        messages.error(request,'invaid activation link')
        return redirect('register')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
    return redirect('login')





def dashboard(request):
    user=request.user
    bookings=Booking.objects.filter(user=user)
    if request.method =='POST':
        profile_pic=request.FILES.get('profile_picture')
        if profile_pic:
            user.profile_picture = profile_pic
            user.save()
            return redirect('dashboard')
        
    context={
      'bookings':bookings,
      'user' :user
    }




    return render(request,'dashboard.html',context)