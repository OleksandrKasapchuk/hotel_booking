from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.index, name="index"),
    path("search-room", booking_views.search_rooms, name="search-rooms"),
	path("show-results//<str:hotel>/<int:capacity>/<str:start_date>/<str:end_date>/", booking_views.show_results, name="show-results"),
    path("book-room//<str:hotel>/<int:capacity>/<str:start_date>/<str:end_date>/", booking_views.book_room, name="book-room"),
    path("booking-info/<int:pk>", booking_views.show_booking_details, name="booking-info")
]