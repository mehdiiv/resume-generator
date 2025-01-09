from skill.forms import SkillCategoryForm
from django.test import TestCase


class SkillCategoryFormTest(TestCase):

    def test_skill_category_create_from_valid_data(self):
        form = SkillCategoryForm(
            {'category': 'example'}
            )
        self.assertTrue(form.is_valid())

    def test_skill_category_create_from_invalid_data(self):
        form = SkillCategoryForm(
            {'category': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}
            )
        self.assertFalse(form.is_valid())
