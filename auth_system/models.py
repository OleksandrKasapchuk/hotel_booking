from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	phone_number = models.CharField(max_length=150)

	def __str__(self):
		return self.username