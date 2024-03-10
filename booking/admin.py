from django.contrib import admin
from booking.models import *

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Hotel)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display =("user", "room", "start_date", "end_date")
    search_fields = ("user",)