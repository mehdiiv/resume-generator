from django.urls import path
from skill.views import (
    SkillCategoryCreateView, SkillCategoriesView,
    SkillCategoryDeleteView, SkillCategoryEditView,
    SkillCategoryDetailView, SkillCreateView,
    SkillDeleteView, SkillEditView
    )


urlpatterns = [
    path('', SkillCategoryCreateView.as_view(),
         name='skill_category_new'),
    path('skill_categories', SkillCategoriesView.as_view(),
         name='skill_categories_list'),
    path('skill_delete/<int:pk_category>', SkillCategoryDeleteView.as_view(),
         name='skill_category_delete'),
    path('<int:pk_category>/skill_edit', SkillCategoryEditView.as_view(),
         name='skill_category_update'),
    path('skill_category/<int:pk_category>', SkillCategoryDetailView.as_view(),
         name='skill_category_detail'),
    path('<int:pk_category>', SkillCreateView.as_view(),
         name='skill_new'),
    path(
        '<int:pk_category>/skill_delete/<int:pk_skill>',
        SkillDeleteView.as_view(),
        name='skill_delete'
         ),
    path(
        '<int:pk_category>/skill_edit/<int:pk_skill>', SkillEditView.as_view(),
        name='skill_edit'
         ),
]
