from django.shortcuts import render
from booking.models import *
# Create your views here.
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