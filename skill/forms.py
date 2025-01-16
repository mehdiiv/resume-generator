from django import forms
from skill.models import SkillCategory, Skill


class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['category']

    def clean(self):
        cleaned_data = self.cleaned_data
        user = self.instance.user
        category = cleaned_data.get("category")

        if SkillCategory.objects.filter(category=category, user=user).exists():
            self.add_error("category", "category with this name already exists for you")
            raise forms.ValidationError("category with this name already exists for you")

        return cleaned_data



class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

    def clean(self):
        cleaned_data = self.cleaned_data
        skill_category_id = self.instance.skill_category_id
        name = cleaned_data.get("name")

        if Skill.objects.filter(name=name, skill_category_id=skill_category_id).exists():
            self.add_error("name", "this skill already exists in this category")
            raise forms.ValidationError("this skill already exists in this category")

        return cleaned_data
