from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    # Add your custom fields here
    phone_number = models.CharField(max_length=20, default='')
    otp = models.CharField(max_length=6, null=True, blank=True) 
    # Specify which fields are required
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.username
