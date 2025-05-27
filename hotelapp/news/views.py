from django.shortcuts import render,redirect
from .models import BlogPost

# Create your views here.

def blogs(request):
    blogs=BlogPost.objects.all()
    context={
        'blogs': blogs
    }
    return render(request,'blog.html',context)