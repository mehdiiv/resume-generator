from django.test import SimpleTestCase
from user_app.views import (
    UserUpdate, UserCreate,
    UserLogin, UserLogout
)
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_user_create_url(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func.view_class, UserCreate)

    def test_user_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, UserLogin)

    def test_user_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, UserLogout)

    def test_user_update_url(self):
        url = reverse('update')
        self.assertEqual(resolve(url).func.view_class, UserUpdate)
