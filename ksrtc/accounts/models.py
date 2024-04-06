from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    # No need to add password field explicitly
    # Django's AbstractUser already includes password field

    def __str__(self):
        return self.username

