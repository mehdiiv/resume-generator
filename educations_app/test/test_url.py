from django.test import SimpleTestCase
from educations_app.views import (
    EducationEditView, EducationCreateView,
    EducationListView, EducationDeleteView,
    EducationDescriptionCreateView, EducationDescriptionEditView,
    EducationDescriptionDeleteView, EducationDetailView
)
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_education_create_url(self):
        url = reverse('education_new')
        self.assertEqual(resolve(url).func.view_class, EducationCreateView)

    def test_education_index_url(self):
        url = reverse('educations_list')
        self.assertEqual(resolve(url).func.view_class, EducationListView)

    def test_education_delete_url(self):
        url = reverse('education_delete', kwargs={'pk_education': 1})
        self.assertEqual(resolve(url).func.view_class, EducationDeleteView)

    def test_education_edit_url(self):
        url = reverse('education_update', kwargs={'pk_education': 1})
        self.assertEqual(resolve(url).func.view_class, EducationEditView)

    def test_education_detail_url(self):
        url = reverse('education_detail', kwargs={'pk_education': 1})
        self.assertEqual(resolve(url).func.view_class, EducationDetailView)

    def test_education_description_create_url(self):
        url = reverse('education_description_new', kwargs={'pk_education': 1})
        self.assertEqual(resolve(url).func.view_class, EducationDescriptionCreateView)

    def test_education_description_edit_url(self):
        url = reverse('education_description_edit', kwargs={'pk_education': 1, 'pk_education_description': 1})
        self.assertEqual(resolve(url).func.view_class, EducationDescriptionEditView)

    def test_education_description_delete_url(self):
        url = reverse('education_description_delete', kwargs={'pk_education': 1, 'pk_education_description': 1})
        self.assertEqual(resolve(url).func.view_class, EducationDescriptionDeleteView)
