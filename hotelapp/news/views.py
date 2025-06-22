from django.shortcuts import render,redirect
from .models import BlogPost

# Create your views here.

def blogs(request):
    blogs=BlogPost.objects.all()
    context={
        'blogs': blogs
    }
    return render(request,'blog.html',context)


def blogs_details(request,id):
    blog_detail=BlogPost.objects.get(id=id)
    context={
        'blog_detail':blog_detail

    }
    return render(request,'blog-details.html',context)