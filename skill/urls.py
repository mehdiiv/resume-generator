from django.urls import path
from skill.views import (
    SkillCategoryCreateView, SkillCategoriesView,
    SkillCategoryDeleteView, SkillCategoryEditView,
    SkillCategoryDetailView, SkillCreateView,
    SkillDeleteView, SkillEditView
    )


urlpatterns = [
    path('new', SkillCategoryCreateView.as_view(),
         name='skill_category_new'),

    path('', SkillCategoriesView.as_view(),
         name='skill_categories_list'),

    path('<int:pk_category>/delete', SkillCategoryDeleteView.as_view(),
         name='skill_category_delete'),

    path('<int:pk_category>/edit', SkillCategoryEditView.as_view(),
         name='skill_category_update'),

    path('<int:pk_category>', SkillCategoryDetailView.as_view(),
         name='skill_category_detail'),

    path('<int:pk_category>/skills', SkillCreateView.as_view(),
         name='skill_new'),

    path(
        '<int:pk_category>/skills/<int:pk_skill>/delete',
        SkillDeleteView.as_view(),

        name='skill_delete'
         ),
    path(
        '<int:pk_category>/skills/<int:pk_skill>/edit', SkillEditView.as_view(),
        name='skill_edit'
         ),
]
