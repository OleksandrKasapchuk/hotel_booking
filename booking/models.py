from django.db import models
from datetime import *
from auth_system.models import CustomUser
from datetime import date


class Hotel(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"Hotel {self.city}"


class Category(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["hotel", "available", "number"]

    def __str__(self):
        return f"{self.hotel} room #{self.number} for {self.capacity}"


class AdditionalFavor(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    add_favors = models.ManyToManyField(AdditionalFavor)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)

    def is_active(self):
        # ending = self.end_date.date()
        now = date.today()
        if self.end_date <= now:
            self.room.available = True
            self.room.save()
            return False
        else:
            return True
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_date", "creation_date"]
    
    def __str__(self):
        return f"{self.user} - {self.room}"


class Review(models.Model):
    text = models.CharField(max_length=150, blank=True, null=True)
    mark = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.mark}"