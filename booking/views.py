from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from random import randint

def index(request):
    if request.method == 'POST':
        user = request.user
        mark = request.POST.get("review-mark")
        text = request.POST.get("review-text")
        Review.objects.create(user=user, mark=mark, text=text)
        return redirect('index')
    else:
        context = {"reviews": Review.objects.all()[:8]}
        return render(
            request,
            "booking/index.html",
            context=context
        )
def search_rooms(request):
    if request.method == "POST":
        hotel = request.POST.get("hotel")
        capacity = request.POST.get("capacity")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        return redirect(f'show-results//{hotel}/{capacity}/{start_date}/{end_date}', hotel=hotel, capacity=capacity, start_date=start_date, end_date=end_date)

def show_results(request, hotel, capacity, start_date, end_date):
    rooms = Room.objects.filter(capacity=capacity, hotel=hotel)
    hotel = Hotel.objects.get(id=hotel)
    context = {"hotel": hotel, "rooms": rooms, "capacity": capacity, "start_date": start_date, "end_date": end_date}
    return render(request, "booking/rooms.html", context)

def book_room(request, hotel, capacity, start_date, end_date):
    if request.user.is_authenticated:
        if request.method == "POST":
            category = request.POST.get('category')
            rooms = Room.objects.filter(category=category, hotel=hotel, capacity=capacity)
            room = rooms[randint(0, len(rooms))]
            room = Room.objects.get(id=room.id)
            room.available = False
            room.save()
            user = request.user
            booking = Booking.objects.create(user=user, room=room, start_date=start_date,end_date=end_date)
            return redirect("booking-info", pk = booking.id)
        else:
            return redirect("index")
    else:
        return redirect("login")

def show_booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
    except Booking.DoesNotExist:
        return HttpResponse (
            "Booking doesn't exist!",
            status=404
        )
    if request.user.id == booking.user.id:
        context = {'booking': booking}
        return render(request, 'booking/booking_info.html', context=context)
