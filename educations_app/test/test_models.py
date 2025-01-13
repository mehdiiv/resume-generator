from django.test import TestCase
from educations_app.models import Education, EducationDescription
from user_app.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='test', last_name='testlast',
            email='test@test.com', password='testpassword'
            )
        self.education = Education.objects.create(
            user_id=self.user.id,
            university='testuniversity', level='testlevel',
            field='testfield',
            date_start='2012-02-02',
            date_end='2013-03-03',
            )
        self.educationdescription = EducationDescription.objects.create(
            education_id = self.education.id,
            description = 'testdescription'
        )

    def test_model_education_cerate(self):
        self.assertEqual(self.education.university, 'testuniversity')
        self.assertEqual(self.education.level, 'testlevel')
        self.assertEqual(self.education.field, 'testfield')
        self.assertEqual(self.education.date_start, '2012-02-02')
        self.assertEqual(self.education.date_end, '2013-03-03')

    def test_model_education_name(self):
        self.assertEqual(self.education._meta.db_table, 'educations')

    def test_model_education_description_cerate(self):
        self.assertEqual(self.educationdescription.description, 'testdescription')

    def test_model_education_description_name(self):
        self.assertEqual(self.educationdescription._meta.db_table, 'education_descriptions')
