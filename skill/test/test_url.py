from django.test import SimpleTestCase
from skill.views import (
    SkillCategoriesView,
    SkillCategoryEditView,
    SkillCategoryDeleteView,
    SkillCategoryCreateView,
    SkillCategoryDetailView
    )
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_category_create_url(self):
        url = reverse('skill_category')
        self.assertEqual(resolve(url).func.view_class, SkillCategoryCreateView)

    def test_categories_index_url(self):
        url = reverse('skill_categories')
        self.assertEqual(resolve(url).func.view_class, SkillCategoriesView)

    def test_categories_delete_url(self):
        url = reverse('skill_category_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryDeleteView)

    def test_category_delete_url(self):
        url = reverse('skill_category_edit', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryEditView)

    def test_category_detail_url(self):
        url = reverse('skill_category_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryDetailView)
