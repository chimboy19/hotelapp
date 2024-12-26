from django.db import models

# Create your models here.


class Rooms(models.Model):
    room_type=models.CharField(max_length=50)
    room_number=models.CharField(max_length=20,unique=True)
    size=models.CharField(max_length=40)
    image=models.ImageField(upload_to='photos/room')
    capacity=models.CharField(max_length=30)
    bed=models.CharField(max_length=100)
    price_per_night=models.IntegerField()
    is_avaliable=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.room_type} {self.room_number}'
    

