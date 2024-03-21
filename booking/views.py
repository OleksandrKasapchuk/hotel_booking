from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from random import randint
from datetime import *

def index(request):
    if request.method == 'POST':
        user = request.user
        mark = request.POST.get("review-mark")
        text = request.POST.get("review-text")
        try:
            if int(mark) > 0 and int(mark) < 6:
                Review.objects.create(user=user, mark=mark, text=text)
        except:
            messages.error(request, "Mark is required")
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
        if hotel is None:
            messages.error(request, "city must be chosen")
        elif capacity is None:
            messages.error(request, "number of guests must be chosen")
        elif start_date == '' or end_date == '':
            messages.error(request, "dates must be chosen")
        elif datetime.strptime(start_date, "%Y-%m-%d").date() < date.today():
            print(datetime.today())
            messages.error(request, "start date must be today or later")
        elif datetime.strptime(end_date, "%Y-%m-%d") <= datetime.strptime(start_date, "%Y-%m-%d"): 
            messages.error(request, "end date must be later than start date")
        else:
            return redirect(f'show-results//{hotel}/{capacity}/{start_date}/{end_date}', hotel=hotel, capacity=capacity, start_date=start_date, end_date=end_date)
        return redirect("index")

def show_results(request, hotel, capacity, start_date, end_date):
    rooms = Room.objects.filter(capacity=capacity, hotel=hotel)
    hotel = Hotel.objects.get(id=hotel)
    context = {"hotel": hotel, "rooms": rooms, "capacity": capacity, "start_date": start_date, "end_date": end_date}
    return render(request, "booking/rooms.html", context=context)

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
