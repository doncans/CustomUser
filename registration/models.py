from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email