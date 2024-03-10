from django.contrib import admin
from booking.models import Booking, Room, Category

admin.site.register(Room)
admin.site.register(Category)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display =("user", "room", "start_time", "end_time")
    search_fields = ("user",)