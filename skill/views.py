from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from skill.forms import SkillCategoryForm, SkillForm
from user_app.views import MyLoginRequiredMixin
from skill.models import SkillCategory, Skill


class SkillCategoriesView(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        categories = request.user.skill_categories.all()
        return render(
            request, 'skill_categories/list.html',
            {'categories': categories}
            )


class SkillCategoryCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skill_categories/new_and_edit.html'

    def get(self, request):
        context = {'form': SkillCategoryForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SkillCategoryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            categories = request.user.skill_categories.all()
            return render(
                request, 'skill_categories/list.html',
                {'categories': categories}
                )
        return render(request, self.template_name, {'form': form})


class SkillCategoryDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_category):
        try:
            request.user.skill_categories.get(id=pk_category).delete()
            return redirect('skill_categories_list')
        except SkillCategory.DoesNotExist:
            return redirect('not_found')


class SkillCategoryEditView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_category):
        try:
            category = request.user.skill_categories.get(id=pk_category)
            context = {'form': SkillCategoryForm(instance=category)}
            return render(
                request, 'skill_categories/new_and_edit.html', context
                )
        except SkillCategory.DoesNotExist:
            return redirect('not_found')

    def post(sefl, request, pk_category):
        category = request.user.skill_categories.get(id=pk_category)
        form = SkillCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('skill_categories_list')
        return render(
            request, 'skill_categories/new_and_edit.html', {'form': form}
            )


class SkillCategoryDetailView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skill_categories/detail.html'

    def get(self, request, pk_category):
        try:
            category = request.user.skill_categories.get(id=pk_category)
            skills = Skill.objects.all().filter(skill_category_id=pk_category)
            context = {
                'category_object': category,
                'skills_ojecsts': skills
                }
            return render(
                request, self.template_name, context
                )
        except SkillCategory.DoesNotExist:
            return redirect('not_found')


class SkillCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skills/new_and_edit.html'

    def get(self, request, pk_category):
        try:
            request.user.skill_categories.get(id=pk_category)
            context = {'form': SkillForm}
            return render(request, self.template_name, context)
        except SkillCategory.DoesNotExist:
            return redirect('not_found')

    def post(self, request, pk_category):
        try:
            request.user.skill_categories.get(id=pk_category)
            form = SkillForm(request.POST)
            form.instance.skill_category_id = pk_category
            if form.is_valid():
                form.save()
                return redirect('skill_category_detail', pk_category)
            return render(request, self.template_name, {'form': form})
        except SkillCategory.DoesNotExist:
            return redirect('not_found')


class SkillDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_category, pk_skill):
        try:
            category = request.user.skill_categories.get(id=pk_category)
            category.skills.get(id=pk_skill).delete()
            return redirect('skill_category_detail', pk_category)
        except (SkillCategory.DoesNotExist, Skill.DoesNotExist):
            return redirect('not_found')


class SkillEditView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skills/new_and_edit.html'

    def get(self, request, pk_category, pk_skill):
        try:
            category = request.user.skill_categories.get(id=pk_category)
            skill = category.skills.get(id=pk_skill)
            form = SkillForm(instance=skill)
            context = {'form': form}
            return render(
                request, self.template_name, context
            )
        except (SkillCategory.DoesNotExist, Skill.DoesNotExist):
            return redirect('not_found')

    def post(self, request, pk_category, pk_skill):
        try:
            category = request.user.skill_categories.get(id=pk_category)
            skill = category.skills.get(id=pk_skill)
            form = SkillForm(request.POST, instance=skill)
            if form.is_valid():
                form.save()
                return redirect('skill_category_detail', pk_category)
            return render(
                request, self.template_name, {'form': form}
            )
        except (SkillCategory.DoesNotExist, Skill.DoesNotExist):
            return redirect('not_found')
