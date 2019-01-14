from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
	pass

class CustomUser(AbstractUser):
    # add additional fields in here

    bio = models.TextField(max_length=400, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username