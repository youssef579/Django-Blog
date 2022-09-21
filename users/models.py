from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, help_text="Required. Only you can see that name")
    email = models.EmailField(unique=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ("full_name",)
    
    objects = UserManager()
    
    def __str__(self):
        return self.full_name + ' ' + self.email