from user_app.forms import  (
    UserCreateForm, LoginForm,
    UserInformationForm
    )
from django.test import TestCase


class UserCreateFormTest(TestCase):

    def test_user_create_from_valid_data(self):
        form = UserCreateForm(
            {'first_name': 'test', 'last_name': 'testi',
             'email': 'test@test.com', 'password': '1',
             'repeat_password': '1'}
            )
        self.assertTrue(form.is_valid())

    def test_user_create_from_invalid_data(self):
        self.user_create_from_invalid_data_emtpy_first_name()
        self.user_create_from_invalid_data_emtpy_last_name()
        self.user_create_from_invalid_data_emtpy_email()
        self.user_create_from_invalid_data_emtpy_password()
        self.user_create_from_invalid_data_emtpy_repeat_password()
        self.user_create_from_invalid_data_not_match_password_repeat_password()

    def user_create_from_invalid_data_emtpy_first_name(self):
        form = UserCreateForm(
            {'last_name': 'testi', 'email': 'test@test.com',
             'password': '1', 'repeat_password': '1'}
            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def user_create_from_invalid_data_emtpy_email(self):
        form = UserCreateForm(
            {'first_name': 'test', 'last_name': 'testi',
             'password': '1', 'repeat_password': '1'}
            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def user_create_from_invalid_data_emtpy_last_name(self):
        form = UserCreateForm(
            {'first_name': 'test', 'email': 'test@test.com',
             'password': '1', 'repeat_password': '1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.')

    def user_create_from_invalid_data_emtpy_password(self):
        form = UserCreateForm(
            {'first_name': 'test',
             'last_name': 'testi', 'email': 'test@test.com',
             'repeat_password': '1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'][0], 'This field is required.')

    def user_create_from_invalid_data_emtpy_repeat_password(self):
        form = UserCreateForm(
            {'first_name': 'test',
             'last_name': 'testi', 'email': 'test@test.com',
             'password': '1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['repeat_password'][0], 'This field is required.')

    def user_create_from_invalid_data_not_match_password_repeat_password(self):
        form = UserCreateForm(
            {'first_name': 'test',
             'last_name': 'testi', 'email': 'test@test.com',
             'password': '1', 'repeat_password': '2'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password'][0], 'Passwords do not match')


class LoginFormTest(TestCase):

    def test_login_form(self):
        form = LoginForm(
            {'email': 'test@test.com', 'password': '1'}
        )
        self.assertTrue(form.is_valid())

    def login_form_invlaid_data(self):
        self.login_form_invlaid_data_emtpy_email()
        self.login_form_invlaid_data_emtpy_password()

    def test_login_form_invlaid_data_emtpy_email(self):
        form = LoginForm(
            {'password': '1'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(['This field is required.'], form.errors['email'])

    def login_form_invlaid_data_emtpy_password(self):
        form = LoginForm(
            {'email': 'test@test.com'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual('This field is required', form.errors['password'])

    def test_detail_form(self):
        form = UserInformationForm(
            {'github_link': 'https://github.com/',
             'linkedin_link': 'https://linkedinlink.com/',
             'phone_number': '+912555464',
             'country': 'iran',
             'city': 'tehran',
             'about_me': 'sdsdadadasdasdasdasdasda',
             'image': ''}
        )
        self.assertTrue(form.is_valid())

    def test_detail_form_invalid_github_link(self):
        form = UserInformationForm(
            {'github_link': 'sssss',
             'linkedin_link': 'https://linkedinlink.com/',
             'phone_number': '+912555464',
             'country': 'iran',
             'city': 'tehran',
             'about_me': 'sdsdadadasdasdasdasdasda',
             'image': ''}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['github_link'][0], 'Enter a valid URL.')

    def test_detail_form_invalid_linkedin_link(self):
        form = UserInformationForm(
            {'github_link': 'https://github.com/',
             'linkedin_link': 'sssss',
             'phone_number': '+912555464',
             'country': 'iran',
             'city': 'tehran',
             'about_me': 'sdsdadadasdasdasdasdasda',
             'image': ''}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['linkedin_link'][0], 'Enter a valid URL.')

    def test_detail_form_invalid_phone_number(self):
        form = UserInformationForm(
            {'github_link': 'https://github.com/',
             'linkedin_link': 'https://linkedinlink.com/',
             'phone_number': 'sdsd',
             'country': 'iran',
             'city': 'tehran',
             'about_me': 'sdsdadadasdasdasdasdasda',
             'image': ''}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['phone_number'][0],
            "Only '+' and numbers are allowed in phone numbers."
              )
