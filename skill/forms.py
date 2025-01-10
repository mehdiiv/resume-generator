from django import forms
from skill.models import SkillCategory, Skill


class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['category']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
