from django.contrib import admin
from .models import Rooms
# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display=('room_number','room_type','size','capacity','price_per_night')
    list_display_links=('room_number',)

admin.site.register(Rooms,RoomsAdmin)