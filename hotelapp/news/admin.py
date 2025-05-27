from django.contrib import admin
from .models import BlogCategory, BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','category','created_at','updated_at')
    list_display_links=('title')


# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogCategory)