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

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_get(self):
        self.client.logout()
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_post(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'first_name': 'test2', 'last_name': 'testi2',
             'email': 'test2@test.com', 'password': '12',
             'repeat_password': '12'}
            )
        self.assertEqual(response.status_code, 302)

    def test_user_create_view_get_invalid_date_empty_email(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'first_name': 'test2', 'last_name': 'testi2',
             'password': '12', 'repeat_password': '12'}
            )
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_get_invalid_date_empty_first_name(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'last_name': 'testi2',
             'email': 'test2@test.com', 'password': '12',
             'repeat_password': '12'}
            )
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_get_invalid_date_empty_last_name(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'first_name': 'test2', 'email': 'test2@test.com',
             'password': '12', 'repeat_password': '12'}
            )
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_get_invalid_date_empty_password(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'first_name': 'test2', 'last_name': 'testi2',
             'email': 'test2@test.com', 'repeat_password': '12'}
            )
        self.assertEqual(response.status_code, 200)

    def test_user_create_view_get_invalid_date_empty_repeat_password(self):
        self.client.logout()
        response = self.client.post(
            reverse('user'),
            {'first_name': 'test2', 'last_name': 'testi2',
             'email': 'test2@test.com', 'password': '12'}
            )
        self.assertEqual(response.status_code, 200)

    def test_user_login_get(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_post(self):
        self.client.logout()
        response = self.client.post(
            reverse('login'), email='test2@test.com', password='12'
            )
        self.assertEqual(response.status_code, 302)

    def test_update_user_get(self):
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 200)

    def test_update_user_post(self):
        response = self.client.post(
            reverse('update'),
            {'first_name': 'updatefirst', 'last_name': 'updatelast',
             'password': '25', 'repeat_password': '25'}
            )
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'updatefirst')
        self.assertEqual(response.status_code, 302)

    def test_update_user_view_post_invalid_empty_first_name(self):
        response = self.client.post(
            reverse('update'),
            {'last_name': 'updatelast',
             'password': '25', 'repeat_password': '25'}
            )
        self.assertEqual(response.status_code, 200)

    def test_update_user_view_post_invalid_empty_last_name(self):
        response = self.client.post(
            reverse('update'),
            {'first_name': 'updatefirst',
             'password': '25', 'repeat_password': '25'}
            )
        self.assertEqual(response.status_code, 200)

    def test_update_user_view_post_invalid_empty_password(self):
        response = self.client.post(
            reverse('update'),
            {'first_name': 'updatefirst',
             'last_name': 'updatelast', 'repeat_password': '25'}
            )
        self.assertEqual(response.status_code, 200)

    def test_update_user_view_post_invalid_empty_repeat_password(self):
        response = self.client.post(
            reverse('update'),
            {'first_name': 'updatefirst',
             'last_name': 'updatelast', 'password': '25'}
            )
        self.assertEqual(response.status_code, 200)

    def test_logout_user_get_view(self):
        logout(self.client)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_detial_user_get_view(self):
        response = self.client.get(reverse('edit_profile_detail'))
        self.assertEqual(response.status_code, 200)
