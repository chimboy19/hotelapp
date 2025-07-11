from django.db import models
from django .contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Rooms(models.Model):
    room_type=models.CharField(max_length=50)
    room_number=models.CharField(max_length=20,unique=True)
    size=models.CharField(max_length=40)
    image=models.ImageField(upload_to='photos/room')
    capacity=models.CharField(max_length=30)
    bed=models.CharField(max_length=100)
    price_per_night=models.IntegerField()
    is_available=models.BooleanField(default=True)
    is_homepage=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.room_type} {self.room_number}'
    



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    guests=models.IntegerField()
    total_price=models.IntegerField()
    reference = models.CharField(max_length=100, blank=True, null=True)
    status= models.CharField(
        max_length=20,
         choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='pending'
    )

    def __str__(self):
        return f'Booking {self.id} - {self.user.username} - {self.room.room_number}'


class ReviewRating(models.Model):
    room= models.ForeignKey(Rooms,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject=models.CharField(max_length=50 , blank=True)
    review=models.TextField(max_length=500 ,blank=True)
    rating=models.FloatField()
    ip= models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
                return self.subject
                    


