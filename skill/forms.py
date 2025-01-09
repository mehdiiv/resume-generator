from django import forms
from skill.models import SkillCategory


class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['category']
