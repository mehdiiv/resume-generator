from django.test import SimpleTestCase
from resume_app.views import UserResumeView
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_resume_display_view_url(self):
        url = reverse('user_resume', kwargs={'full_name': 'za-za'})
        self.assertEqual(resolve(url).func.view_class, UserResumeView)
