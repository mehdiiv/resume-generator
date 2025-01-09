from django.db import models
from user_app.models import User


class SkillCategory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='skill_categories'
        )
    category = models.CharField(
        max_length=32, blank=False,
        unique=True
        )

    class Meta:
        db_table = 'skill_categories'
