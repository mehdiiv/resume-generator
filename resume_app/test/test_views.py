from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
             first_name='test', last_name='testi',
             email='test@test.com'
        )
        self.user.set_password('1')
        self.user.save()
        self.client = Client()
        self.client.login(
            email='test@test.com', password='1'
        )

    def test_resume_get_view_login(self):
        response = self.client.get(
            reverse('user_resume', kwargs={'full_name': self.user.full_name()})
            )
        self.assertEqual(response.status_code, 200)

    def test_resume_get_view_logout(self):
        response = self.client.get(reverse(
            'user_resume', kwargs={'full_name': self.user.full_name()})
            )
        self.assertEqual(response.status_code, 200)

    def test_resume_get_view_login_invalid_full_name(self):
        response = self.client.get(
            reverse('user_resume', kwargs={'full_name': 'none-none'})
            )
        self.assertEqual(response.status_code, 302)

    def test_resume_get_view_logout_invalid_full_name(self):
        logout(self.client)
        response = self.client.get(
            reverse('user_resume', kwargs={'full_name': 'none-none'})
            )
        self.assertEqual(response.status_code, 302)
