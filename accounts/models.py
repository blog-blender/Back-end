from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    profile_pic = CloudinaryField("image",overwrite=True,format="jpg",null=True, blank=True)
    user_banner_pic = CloudinaryField("image",overwrite=True,format="jpg",null=True, blank=True)

