from educations_app.forms import EducationForm, EducationDescriptionForm
from django.test import TestCase


class EducationFormTest(TestCase):

    def test_education_create_from_valid_data(self):
        form = EducationForm(
            {'university': 'testuniversity',
             'level': 'testlevel', 'date_start': '2013-03-03',
             'field': 'testfield',
             'date_end': '2012-02-02'}
            )
        self.assertTrue(form.is_valid())

    def test_education_create_from_invalid_data(self):
        form = EducationForm(
            {'university': 'testuniversity',
             'level': 'testlevel', 'date_start': 'xyz',
             'date_end': '2012-02-02'}
            )
        self.assertFalse(form.is_valid())


class EducationDescriptionFormTest(TestCase):

    def test_education_description_create_from_valid_data(self):
        form = EducationDescriptionForm(
            {'description': 'exampledescription'}
            )
        self.assertTrue(form.is_valid())
