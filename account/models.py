from django.contrib.auth.models import AbstractUser
from django.db import models


class customUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, unique=True,  blank=False)
    birthday = models.CharField(max_length=15, blank=False)
    phone = models.CharField(max_length=10)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "phone"]

