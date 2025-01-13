from django import forms
from educations_app.models import Education, EducationDescription


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'level', 'field', 'date_start', 'date_end']


class EducationDescriptionForm(forms.ModelForm):
    class Meta:
        model = EducationDescription
        fields = ['description']
