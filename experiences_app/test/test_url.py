from django.test import SimpleTestCase
from experiences_app.views import (
    ExperienceEditView, ExperienceCreateView,
    ExperienceListView, ExperienceDeleteView
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

    def test_category_edit_url(self):
        url = reverse('experience_update', kwargs={'pk_experience': 1})
        self.assertEqual(resolve(url).func.view_class, ExperienceEditView)
