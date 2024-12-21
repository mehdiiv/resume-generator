from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=128, blank=False, null=False)
    password = models.CharField(max_length=68, blank=False, name=False)
    create_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'users'
