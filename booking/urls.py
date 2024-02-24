from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.index, name="index"),
    path("rooms/", booking_views.show_rooms, name="rooms"),
    path("rooms/<int:room_id>", booking_views.get_room, name="room_details"),
    path("search-room/", booking_views.search_room, name="search-room")
]