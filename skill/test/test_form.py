from skill.forms import SkillCategoryForm, SkillForm
from django.test import TestCase
from user_app.models import User
from skill.models import SkillCategory


class SkillCategoryFormTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            first_name='test', last_name='testlast',
            email='test@test.com', password='testpassword'
        )

        self.skill_category = SkillCategory.objects.create(
            user=self.user,
            category='Programming'
        )

    def test_skill_category_create_form_valid_data(self):
        form = SkillCategoryForm(data={'category': 'Design'}, instance=self.skill_category)
        self.assertTrue(form.is_valid())

    def test_skill_category_create_form_invalid_data(self):
        form = SkillCategoryForm(data={'category': 'Programming'}, instance=self.skill_category)
        self.assertFalse(form.is_valid())


class SkillFormTest(TestCase):

    def test_skill_category_create_form_valid_data(self):
        form = SkillForm(
            {'name': 'example'}
            )
        self.assertTrue(form.is_valid())

    def test_skill_category_create_form_invalid_data(self):
        form = SkillForm(
            {'name': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}
            )
        self.assertFalse(form.is_valid())
