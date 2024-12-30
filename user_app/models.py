from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=68, blank=False)
    last_name = models.CharField(max_length=68, blank=False)
    email = models.EmailField(
        unique=True, max_length=128, blank=False, null=False
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'
