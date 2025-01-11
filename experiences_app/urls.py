from django.urls import path
from experiences_app.views import (
    ExperienceListView, ExperienceCreateView,
    ExperienceDeleteView, ExperienceEditView
    )


urlpatterns = [
    path('', ExperienceCreateView.as_view(),
         name='experience_new'),
    path('skill_categories', ExperienceListView.as_view(),
         name='experiences_list'),
    path('<int:pk_experience>/experience_delete/', ExperienceDeleteView.as_view(),
         name='experience_delete'),
    path('<int:pk_experience>/experience_edit', ExperienceEditView.as_view(),
         name='experience_update'),
]
