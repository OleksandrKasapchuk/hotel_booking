from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.index, name="index"),
    path("hotel-info/", booking_views.hotel_info, name="hotel-info"),
    path("user-info/<int:pk>", booking_views.user_info, name="user-info"),
    path("sign-in/", booking_views.sign_in, name="sign-in"),
    path("rooms/", booking_views.show_rooms, name="rooms"),
    path("rooms/<int:room_id>", booking_views.get_room, name="room-details"),
    path("search-room/", booking_views.search_room, name="search-room"),
    path("book-room/<int:room_id>", booking_views.book_room, name="book-room"),
    path("booking-info/<int:pk>", booking_views.show_booking_details, name="booking-info")
]