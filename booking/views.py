from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse

def index(request):
    return render(
        request,
        template_name="booking/index.html"
    )
def show_rooms(request):
    context = {"rooms": Room.objects.all()}
    return render(
        request,
        template_name="booking/rooms.html",
        context=context
    )

def get_room(request, room_id):
    context = {"room": Room.objects.get(id=room_id)}
    return render(
        request,
        template_name="booking/room_details.html",
        context=context
    )

def search_room(request):
    if request.method == "POST":
        room_capacity = request.POST.get("room-capacity")
        try:
            rooms = Room.objects.filter(capacity=room_capacity)
        except ValueError:
            return HttpResponse("Invalid value for room-capacity!", status=400)

        context = {"rooms":rooms}
        return render(
            request,
            template_name="booking/filter_rooms.html",
            context=context
        )          
    else:
        return render(request, "booking/search_room.html")