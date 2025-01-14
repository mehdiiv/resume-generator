from django.urls import path
from educations_app.views import (
    EducationListView, EducationCreateView,
    EducationDeleteView, EducationEditView,
    EducationDescriptionCreateView, EducationDescriptionEditView,
    EducationDescriptionDeleteView, EducationDetailView
    )


urlpatterns = [
    path('new', EducationCreateView.as_view(),
         name='education_new'),

    path('', EducationListView.as_view(),
         name='educations_list'),

    path('<int:pk_education>/delete/', EducationDeleteView.as_view(),
         name='education_delete'),

    path('<int:pk_education>/edit', EducationEditView.as_view(),
         name='education_update'),

    path('<int:pk_education>', EducationDetailView.as_view(),
         name='education_detail'),

    path('<int:pk_education>/education_descriptions', EducationDescriptionCreateView.as_view(),
         name='education_description_new'),

    path(
        '<int:pk_education>/education_descriptions/<int:pk_education_description>/delete',
        EducationDescriptionDeleteView.as_view(),
        name='education_description_delete'
         ),
    path(
        '<int:pk_education>/education_descriptions/<int:pk_education_description>/edit', EducationDescriptionEditView.as_view(),
        name='education_description_edit'
         ),
]
