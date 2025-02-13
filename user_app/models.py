from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=68, blank=False)
    last_name = models.CharField(max_length=68, blank=False)
    email = models.EmailField(
        unique=True, max_length=128, blank=False, null=False
        )
    title = models.CharField(
        max_length=64, blank=True, null=True
    )
    github_link = models.URLField(
        max_length=128, blank=True, null=True
        )
    linkedin_link = models.URLField(
        max_length=128, blank=True, null=True
        )
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )
    country = models.CharField(
        max_length=30, blank=True, null=True
    )
    city = models.CharField(
        max_length=30, blank=True, null=True
    )
    image = models.ImageField(
        upload_to='user_images/',
        storage=FileSystemStorage(location='media/'),
        blank=True, null=True
        )
    about_me = models.TextField(
        max_length=512, blank=True, null=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        unique_together = ['first_name', 'last_name']
        db_table = 'users'

    def full_name(self):
        return f"{self.first_name}-{self.last_name}"
