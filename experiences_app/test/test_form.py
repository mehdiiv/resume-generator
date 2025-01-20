from experiences_app.forms import ExperienceForm, ExperienceDescriptionForm
from django.test import TestCase


class ExperienceFormTest(TestCase):

    def test_experience_create_form_valid_data(self):
        form = ExperienceForm(
            {'title': 'testtitle',
             'role': 'testrole', 'start_date': '2013-03-03',
             'end_date': '2012-02-02'}
            )
        self.assertTrue(form.is_valid())

    def test_experience_create_form_invalid_data(self):
        form = ExperienceForm(
            {'title': 'testtitle',
             'role': 'testrole', 'start_date': 'xyz',
             'end_date': '2012-02-02'}
            )
        self.assertFalse(form.is_valid())


class ExperienceDescriptionFormTest(TestCase):

    def test_experience_description_create_form_valid_data(self):
        form = ExperienceDescriptionForm(
            {'description': 'exampledescription'}
            )
        self.assertTrue(form.is_valid())
