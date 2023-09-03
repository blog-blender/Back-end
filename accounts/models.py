from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    user_banner_pic = models.ImageField(upload_to='profile_banner/', blank=True, null=True)
    def __str__(self):
        return self.username
