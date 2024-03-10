from django.contrib import admin
from booking.models import *

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Review)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display =("user", "room", "start_time", "end_time")
    search_fields = ("user",)