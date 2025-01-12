from django.test import TestCase
from experiences_app.models import Experience, ExperienceDescription
from user_app.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='test', last_name='testlast',
            email='test@test.com', password='testpassword'
            )
        self.experience = Experience.objects.create(
            user_id=self.user.id,
            title='testtitle', role='testrole',
            start_date='2012-02-02',
            end_date='2013-03-03',
            )
        self.experiencedescription = ExperienceDescription.objects.create(
            experience_id = self.experience.id,
            description = 'testdescription'
        )

    def test_model_experience_cerate(self):
        self.assertEqual(self.experience.title, 'testtitle')
        self.assertEqual(self.experience.role, 'testrole')
        self.assertEqual(self.experience.start_date, '2012-02-02')
        self.assertEqual(self.experience.end_date, '2013-03-03')

    def test_model_experience_name(self):
        self.assertEqual(self.experience._meta.db_table, 'experiences')

    def test_model_experience_description_cerate(self):
        self.assertEqual(self.experiencedescription.description, 'testdescription')

    def test_model_experience_description_name(self):
        self.assertEqual(self.experiencedescription._meta.db_table, 'experience_descriptions')
