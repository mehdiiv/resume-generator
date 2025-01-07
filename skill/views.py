from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from skill.forms import SkillCategoryForm
from user_app.views import MyLoginRequiredMixin
from skill.models import SkillCategory


class SkillCategoriesView(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        categories = request.user.skill_categories.all()
        return render(
            request, 'skill/index_skill_categories.html',
            {'categories': categories}
            )


class SkillCategoryCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skill/skill_category_form.html'

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
                request, 'skill/index_skill_categories.html',
                {'categories': categories}
                )
        return render(request, self.template_name, {'form': SkillCategoryForm})


class SkillCategoryDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk):
        try:
            request.user.skill_categories.get(id=pk).delete()
            return redirect('skill_categories')
        except SkillCategory.DoesNotExist:
            return redirect('not_found')


class SkillCategoryEditView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk):
        try:
            category = request.user.skill_categories.get(id=pk)
            context = {'form': SkillCategoryForm(instance=category)}
            return render(
                request, 'skill/skill_category_edit_form.html', context
                )
        except SkillCategory.DoesNotExist:
            return redirect('not_found')

    def post(sefl, request, pk):
        category = request.user.skill_categories.get(id=pk)
        form = SkillCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('skill_categories')
        return render(
            request, 'skill/skill_category_edit_form.html', {'form': category}
            )


class SkillCategoryDetailView(MyLoginRequiredMixin, TemplateView):
    template_name = 'skill/detail_skill_category.html'

    def get(self, request, pk):
        try:
            category = request.user.skill_categories.get(id=pk)
            context = {'category_object': category}
            return render(
                request, self.template_name, context
                )
        except SkillCategory.DoesNotExist:
            return redirect('not_found')
