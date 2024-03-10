from django.db import models
from datetime import *
from auth_system.models import CustomUser
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["available", "number"]

    def __str__(self):
        return f"Room #{self.number} for {self.capacity}"


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        ending = self.end_time.date()
        now = date.today()
        if ending <= now:
            self.room.available = True
            self.room.save()
            return False
        else:
            return True
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time", "creation_time"]
    
    def __str__(self):
        return f"{self.user} - {self.room}"