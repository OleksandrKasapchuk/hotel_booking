from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(
        request,
        "booking/index.html"
    )

def hotel_info(request):
    return render(
        request,
        "booking/hotel_info.html"
    )

def show_rooms(request):
    context = {"rooms": Room.objects.all(), "bookings": Booking.objects.all()}
    for booking in Booking.objects.all():
        booking.is_active()
    return render(
        request,
        template_name="booking/rooms.html",
        context=context
    )

def get_room(request, room_id):
    context = {"room": Room.objects.get(id=room_id)}
    return render(
        request,
        "booking/room_details.html",
        context=context
    )

def search_room(request):
    if request.method == "POST":
        room_capacity = request.POST.get("room-capacity")
        try:
            rooms = Room.objects.filter(capacity=room_capacity)
            context = {"rooms":rooms}
            for booking in Booking.objects.all():
                booking.is_active()
        except ValueError:
            messages.success(request, ("Invalid value for room-capacity!"))
            context = {}
        return render(
            request,
            "booking/rooms.html",
            context=context
            )       
    else:
        return render(request, "booking/search_room.html")

def book_room(request, room_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            room = Room.objects.get(id=room_id)
            room.available = False
            room.save()
            user = request.user
            booking = Booking.objects.create(user=user, room=room, start_time=start_time,end_time=end_time)
            return redirect("booking-info", pk = booking.id)
        else:
            context = {"room": Room.objects.get(id=room_id)}
            return render(request, template_name="booking/book_room.html", context=context)
    else:
        return redirect("login")

def show_booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {'booking': booking}
        return render(request, 'booking/booking_info.html', context=context)
    except Booking.DoesNotExist:
        return HttpResponse (
            "Booking doesn't exist!",
            status=404
        )
