from django.db import models
from user_app.models import User


class SkillCategory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='skill_categories'
        )
    category = models.CharField(
        max_length=32, blank=False
        )

    class Meta:
        unique_together = ['user', 'category']
        db_table = 'skill_categories'


class Skill(models.Model):
    skill_category = models.ForeignKey(
        SkillCategory, on_delete=models.CASCADE,
        related_name='skills'
        )
    name = models.CharField(
        max_length=32, blank=False
        )

    class Meta:
        unique_together = ['skill_category', 'name']
        db_table = 'skills'
