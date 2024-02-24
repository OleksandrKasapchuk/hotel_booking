from django.contrib import admin
from booking.models import Booking, Room, User

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(User)