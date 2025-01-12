from django.test import SimpleTestCase
from experiences_app.views import (
    ExperienceEditView, ExperienceCreateView,
    ExperienceListView, ExperienceDeleteView,
    ExperienceDescriptionCreateView, ExperienceDescriptionEditView,
    ExperienceDescriptionDeleteView, ExperienceDetailView
)
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_experience_create_url(self):
        url = reverse('experience_new')
        self.assertEqual(resolve(url).func.view_class, ExperienceCreateView)

    def test_experience_index_url(self):
        url = reverse('experiences_list')
        self.assertEqual(resolve(url).func.view_class, ExperienceListView)

    def test_experience_delete_url(self):
        url = reverse('experience_delete', kwargs={'pk_experience': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceDeleteView)

    def test_experience_edit_url(self):
        url = reverse('experience_update', kwargs={'pk_experience': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceEditView)

    def test_experience_detail_url(self):
        url = reverse('experience_detail', kwargs={'pk_experience': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceDetailView)

    def test_experience_description_create_url(self):
        url = reverse('description_new', kwargs={'pk_experience': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceDescriptionCreateView)

    def test_experience_description_edit_url(self):
        url = reverse('description_edit', kwargs={'pk_experience': 1, 'pk_description': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceDescriptionEditView)

    def test_experience_description_delete_url(self):
        url = reverse('description_delete', kwargs={'pk_experience': 1, 'pk_description': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceDescriptionDeleteView)
