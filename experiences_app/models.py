from django.db import models
from user_app.models import User


class Experience(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='experiences'
        )
    title = models.CharField(
        max_length=32, blank=False,
        unique=True
        )
    role = models.CharField(
        max_length=128, blank=False,
        unique=True
        )
    start_date = models.DateField()
    end_date = models.DateField(
        null=True, blank=True
        )

    class Meta:
        db_table = 'experiences'
