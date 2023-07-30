from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    # bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username