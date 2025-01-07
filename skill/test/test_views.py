from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User
from skill.models import SkillCategory


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
             first_name='test', last_name='testi',
             email='test@test.com'
        )
        self.user.set_password('1')
        self.user.save()
        self.client = Client()
        self.client.login(
            email='test@test.com', password='1'
        )
        self.skillcategory = SkillCategory.objects.create(
            user=self.user, category='testcategory'
        )

    def test_create_skillcategory_get_view(self):
        response = self.client.get(reverse('skill_category'))
        self.assertEqual(response.status_code, 200)

    def test_create_skillcategory_post_view(self):
        response = self.client.post(
            reverse('skill_category'),
            {'category': 'testcategory2'}
            )
        self.assertEqual(response.status_code, 200)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(2, categories)

    def test_create_skillcategory_get_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('skill_category'))
        self.assertEqual(response.status_code, 302)

    def test_create_skillcategory_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse('skill_category'),
            {'category': 'testcategory2'}
            )
        self.assertEqual(response.status_code, 302)

    def test_index_skill_categories_View(self):
        response = self.client.get(reverse('skill_categories'))
        self.assertEqual(response.status_code, 200)

    def test_index_skill_categories_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('skill_categories'))
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(1, categories)

    def test_skill_category_edit_view_get(self):
        response = self.client.get(
            reverse('skill_category_edit', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 200)

    def test_skill_category_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse('skill_category_edit', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 302)

    def test_skill_category_edit_view_post(self):
        response = self.client.post(reverse(
            'skill_category_edit', kwargs={'pk': self.user.id}),
            {'category': 'updatecategory'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            SkillCategory.objects.get(user=self.user).category,
            'updatecategory'
            )

    def test_skill_category_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'skill_category_edit', kwargs={'pk': self.user.id}),
            {'category': 'updatecategory'})
        self.assertEqual(response.status_code, 302)

    def test_skill_category_delete_view(self):
        response = self.client.get(
            reverse('skill_category_delete', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(0, categories)

    def test_skill_category_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse('skill_category_delete', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(1, categories)

    def test_skill_category_detail_view(self):
        response = self.client.get(
            reverse('skill_category_detail', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 200)

    def test_skill_category_detail_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse('skill_category_detail', kwargs={'pk': self.user.id})
            )
        self.assertEqual(response.status_code, 302)
