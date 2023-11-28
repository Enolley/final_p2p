from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=100, default="is_client")
    course = models.CharField(max_length=100, default="None")
    profile = models.ImageField(upload_to="uploads/users", default="uploads/users/profile.png")
    status = models.CharField(max_length=100, default="is_active")