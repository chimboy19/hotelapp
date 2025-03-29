from django.shortcuts import render,redirect

# Create your views here.

def blogs(request):
    return render(request,'blog.html')