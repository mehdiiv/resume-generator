from django import forms
from educations_app.models import Education, EducationDescription


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'level', 'field', 'start_date', 'end_date']


class EducationDescriptionForm(forms.ModelForm):
    class Meta:
        model = EducationDescription
        fields = ['description']
