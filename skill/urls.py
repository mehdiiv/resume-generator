from django.urls import path
from django.views.generic import TemplateView
from skill.views import (
    SkillCategoryCreateView, SkillCategoriesView,
    SkillCategoryDeleteView, SkillCategoryEditView,
    SkillCategoryDetailView
    )


urlpatterns = [
    path(
        '', SkillCategoryCreateView.as_view(),
        name='skill_category'),
    path('Categories/', SkillCategoriesView.as_view(),
         name='skill_categories'),
    path('<int:pk>/delete/', SkillCategoryDeleteView.as_view(),
         name='skill_category_delete'),
    path('<int:pk>/edit/', SkillCategoryEditView.as_view(),
         name='skill_category_edit'),
    path('404/', TemplateView.as_view(template_name='skill/404.html'),
         name='not_found'),
    path('<int:pk>/categoir/', SkillCategoryDetailView.as_view(),
         name='skill_category_detail')
]
