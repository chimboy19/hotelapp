from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify




class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=120 ,unique=True, blank=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    blog_image=models.ImageField(upload_to='blog_images/',null=True , blank=True)
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
