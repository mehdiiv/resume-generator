from django.db import models
from user_app.models import User
from django.utils.formats import date_format


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
    start_date = models.DateField(blank=False)
    end_date = models.DateField(
        null=True, blank=True
        )


    class Meta:
        db_table = 'educations'

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


class EducationDescription(models.Model):
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE,
        related_name='education_descriptions'
    )
    description = models.TextField(
        max_length=512, blank=False
        )

    class Meta:
        db_table = 'education_descriptions'
