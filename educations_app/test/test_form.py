from educations_app.forms import EducationForm, EducationDescriptionForm
from django.test import TestCase


class EducationFormTest(TestCase):

    def test_education_create_form_valid_data(self):
        form = EducationForm(
            {'university': 'testuniversity',
             'level': 'testlevel', 'start_date': '2013-03-03',
             'field': 'testfield',
             'end_date': '2012-02-02'}
            )
        self.assertTrue(form.is_valid())

    def test_education_create_form_invalid_data(self):
        form = EducationForm(
            {'university': 'testuniversity',
             'level': 'testlevel', 'start_date': 'xyz',
             'end_date': '2012-02-02'}
            )
        self.assertFalse(form.is_valid())


class EducationDescriptionFormTest(TestCase):

    def test_education_description_create_form_valid_data(self):
        form = EducationDescriptionForm(
            {'description': 'exampledescription'}
            )
        self.assertTrue(form.is_valid())
