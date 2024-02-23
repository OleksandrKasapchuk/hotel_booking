from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.show_rooms, name="rooms"),
    path("<int:room_id>", booking_views.get_room, name="room_details")
]