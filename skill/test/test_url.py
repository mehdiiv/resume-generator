from django.test import SimpleTestCase
from skill.views import (
    SkillCategoriesView, SkillCategoryEditView,
    SkillCategoryDeleteView, SkillEditView,
    SkillCategoryCreateView, SkillCategoryDetailView,
    SkillCreateView, SkillDeleteView,
    )
from django.urls import resolve, reverse


class UrlTest(SimpleTestCase):
    def test_category_create_url(self):
        url = reverse('skill_category_new')
        self.assertEqual(resolve(url).func.view_class, SkillCategoryCreateView)

    def test_categories_index_url(self):
        url = reverse('skill_categories_list')
        self.assertEqual(resolve(url).func.view_class, SkillCategoriesView)

    def test_categories_delete_url(self):
        url = reverse('skill_category_delete', kwargs={'pk_category': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryDeleteView)

    def test_category_edit_url(self):
        url = reverse('skill_category_update', kwargs={'pk_category': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryEditView)

    def test_category_detail_url(self):
        url = reverse('skill_category_detail', kwargs={'pk_category': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCategoryDetailView)

    def test_skill_create_url(self):
        url = reverse('skill_new', kwargs={'pk_category': 1})
        self.assertEqual(resolve(url).func.view_class, SkillCreateView)

    def test_skill_edit_url(self):
        url = reverse('skill_edit', kwargs={'pk_category': 1, 'pk_skill': 1})
        self.assertEqual(resolve(url).func.view_class, SkillEditView)

    def test_skill_delete_url(self):
        url = reverse('skill_delete', kwargs={'pk_category': 1, 'pk_skill': 1})
        self.assertEqual(resolve(url).func.view_class, SkillDeleteView)
