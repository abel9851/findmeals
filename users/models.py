from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(default="", blank=True)
