from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
        booking.room_available()
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
        except ValueError:
            messages.success(request, ("Invalid value for room-capacity!"))
            context = {}
        return render(
            request,
            "booking/filter_rooms.html",
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

def register_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            name = request.POST.get('first_name')
            surname = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            new_user = User.objects.create_user(username=username, first_name=name, last_name=surname, email=email, password=password)
            new_user.save()
            user = authenticate(username=username, first_name=name, last_name=surname, email=email, password=password)
            login(request, user)

            return redirect("index")
        else:
            return render(request, "booking/register.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, ("You have been succesfully logged in"))
                return redirect("index")
            else:
                messages.success(request, ("There was an error logging in, try again!"))
                return redirect("login")
            
        else:
            return render(request, "booking/login.html")
        

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect("index")

def user_info(request, pk):
    try:
        user = User.objects.get(id=pk)
        bookings = Booking.objects.all()
        context = {'user': user, "bookings": bookings}
        return render(request, 'booking/user_info.html', context=context)
    except User.DoesNotExist:
        return HttpResponse (
            "User doesn't exist!",
            status=404
        )

def edit_user(request, user_id):
    if request.method == 'POST':
        username = request.POST.get("username")
        name = request.POST.get('first_name')
        surname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.get(id=user_id)
        user.username=username 
        user.email=email
        user.password=password
        user.first_name=name
        user.last_name=surname
        user.save()

        return redirect(f"/user-info/{user_id}")
    else:
        return render(request, "booking/edit_user.html")

def change_password(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        password = request.POST.get('password')
        new_password = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        validated = check_password(password, user.password)
        if validated:
            if new_password == new_password2:
                user.set_password(new_password)
                user.save()
                login(request, user)
                messages.success(request, ("Password has been changed"))
            else:
                messages.success(request, ("Passwords do not match"))
                return redirect(f'/change-password/{user_id}')
        else:
            messages.success(request, ("Incorrect password"))
            return redirect(f'/change-password/{user_id}')
        return redirect(f"/user-info/{user_id}")
    else:
        return render(request, "booking/change_password.html")