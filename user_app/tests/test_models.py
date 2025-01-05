from django.test import TestCase
from user_app.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='test', last_name='testlast',
            email='test@test.com', password='testpassword',
            github_link='https://github.com/',
            linkedin_link='https://linkedinlink.com/',
            phone_number='+912555464',
            country='iran',
            city='tehran',
            about_me='sdsdadadasdasdasdasdasda',
            image=''
            )

    def test_model_user_cerate(self):
        self.assertEqual(self.user.first_name, 'test')
        self.assertEqual(self.user.last_name, 'testlast')
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.password, 'testpassword')
        self.assertEqual(self.user.github_link, 'https://github.com/')
        self.assertEqual(self.user.linkedin_link, 'https://linkedinlink.com/')
        self.assertEqual(self.user.phone_number, '+912555464')
        self.assertEqual(self.user.country, 'iran')
        self.assertEqual(self.user.city, 'tehran')
        self.assertEqual(self.user.about_me, 'sdsdadadasdasdasdasdasda')

    def test_user_table_name(self):
        self.assertEqual(self.user._meta.db_table, 'users')
