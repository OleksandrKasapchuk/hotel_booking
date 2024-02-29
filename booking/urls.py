from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.index, name="index"),
    path("hotel-info/", booking_views.hotel_info, name="hotel-info"),
    path("user-info/<int:pk>", booking_views.user_info, name="user-info"),
    path("register/", booking_views.register_user, name="register"),
    path("login/", booking_views.login_user, name="login"),
    path("logout/", booking_views.logout_user, name="logout"),
    path("rooms/", booking_views.show_rooms, name="rooms"),
    path("rooms/<int:room_id>", booking_views.get_room, name="room-details"),
    path("search-room/", booking_views.search_room, name="search-room"),
    path("book-room/<int:room_id>", booking_views.book_room, name="book-room"),
    path("booking-info/<int:pk>", booking_views.show_booking_details, name="booking-info")
]