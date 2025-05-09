from django.contrib import admin
from .models import Rooms,Booking
# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display=('room_number','room_type','size','capacity','price_per_night')
    list_display_links=('room_number',)


class BookingAdmin(admin.ModelAdmin):
    list_display=('user','room','check_in','check_out','total_price','status')


admin.site.register(Rooms,RoomsAdmin)
admin.site.register(Booking,BookingAdmin)