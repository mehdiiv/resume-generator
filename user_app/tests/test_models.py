from django.test import TestCase
from user_app.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com', password='testpassword')

    def test_model_user_cerate(self):
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.password, 'testpassword')

    def test_user_table_name(self):
        self.assertEqual(self.user._meta.db_table, 'users')
