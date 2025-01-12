from django import forms
from experiences_app.models import Experience, ExperienceDescription


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'role', 'start_date', 'end_date']


class ExperienceDescriptionForm(forms.ModelForm):
    class Meta:
        model = ExperienceDescription
        fields = ['description']
