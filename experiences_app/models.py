from django.db import models
from user_app.models import User
from django.utils.formats import date_format


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
        )
    start_date = models.DateField()
    end_date = models.DateField(
        null=True, blank=True
        )

    class Meta:
        unique_together = ['user', 'title']
        db_table = 'experiences'

    def start_date_year_month(self):
        return date_format(self.start_date, "Y F")

    def end_date_year_month(self):
        if self.end_date:
            return date_format(self.end_date, "Y F")
        return 'now'

    def start_date_form(self):
        return date_format(self.start_date, "Y-m-d")

    def end_date_form(self):
        if self.end_date:
            return date_format(self.end_date, "Y-m-d")
        return 'now'


class ExperienceDescription(models.Model):
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE,
        related_name='experience_descriptions'
    )
    description = models.TextField(
        max_length=1024, blank=False
        )

    class Meta:
        db_table = 'experience_descriptions'
