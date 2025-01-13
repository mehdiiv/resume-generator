from django.urls import path
from experiences_app.views import (
    ExperienceListView, ExperienceCreateView,
    ExperienceDeleteView, ExperienceEditView,
    ExperienceDescriptionCreateView, ExperienceDescriptionEditView,
    ExperienceDescriptionDeleteView, ExperienceDetailView
    )


urlpatterns = [
    path('new', ExperienceCreateView.as_view(),
         name='experience_new'),

    path('', ExperienceListView.as_view(),
         name='experiences_list'),

    path('<int:pk_experience>/delete/', ExperienceDeleteView.as_view(),
         name='experience_delete'),

    path('<int:pk_experience>/edit', ExperienceEditView.as_view(),
         name='experience_update'),

    path('<int:pk_experience>', ExperienceDetailView.as_view(),
         name='experience_detail'),

    path('<int:pk_experience>/experience_descriptions', ExperienceDescriptionCreateView.as_view(),
         name='experience_description_new'),

    path(
        '<int:pk_experience>/experience_descriptions/<int:pk_experience_description>/delete',
        ExperienceDescriptionDeleteView.as_view(),
        name='experience_description_delete'
         ),
    path(
        '<int:pk_experience>/experience_descriptions/<int:pk_experience_description>/edit', ExperienceDescriptionEditView.as_view(),
        name='experience_description_edit'
         ),
]
