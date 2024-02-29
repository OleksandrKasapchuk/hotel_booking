from django.db import models
from datetime import *
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["available", "number", "-price"]

    def __str__(self):
        return f"Room #{self.number} for {self.capacity}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time", "creation_time"]
    
    def __str__(self):
        return f"{self.user} - {self.room}"