from django.db import models
from user_app.models import User


class Education(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='educations'
        )
    university = models.CharField(
        max_length=64, blank=False
        )
    level = models.CharField(
        max_length=64, blank=False
        )
    field = models.CharField(
        max_length=128, blank=False
        )
    date_start = models.DateField(blank=False)
    date_end = models.DateField(
        null=True, blank=True
        )

    class Meta:
        db_table = 'educations'

class EducationDescription(models.Model):
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE,
        related_name='education_descriptions'
    )
    description = models.TextField(
        max_length=512, blank=False,
        unique=True
        )

    class Meta:
        db_table = 'education_descriptions'
