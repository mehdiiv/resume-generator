from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User
from skill.models import SkillCategory, Skill


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
        self.skill = Skill.objects.create(
            skill_category_id=self.skillcategory.id, name='testname'
            )

    def test_create_skill_category_get_view(self):
        response = self.client.get(reverse('skill_category_new'))
        self.assertEqual(response.status_code, 200)

    def test_create_skill_category_post_view(self):
        response = self.client.post(
            reverse('skill_category_new'),
            {'category': 'testcategory2'}
            )
        self.assertEqual(response.status_code, 200)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(2, categories)

    def test_create_skill_category_get_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('skill_category_new'))
        self.assertEqual(response.status_code, 302)

    def test_create_skill_category_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse('skill_category_new'),
            {'category': 'testcategory2'}
            )
        self.assertEqual(response.status_code, 302)

    def test_index_skill_categories_View(self):
        response = self.client.get(reverse('skill_categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_index_skill_categories_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('skill_categories_list'))
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(1, categories)

    def test_skill_category_edit_view_get(self):
        response = self.client.get(
            reverse(
                'skill_category_update',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_skill_category_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_category_update',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_skill_category_edit_view_post(self):
        response = self.client.post(reverse(
            'skill_category_update',
            kwargs={'pk_category': self.skillcategory.id}
            ),
            {'category': 'updatecategory'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            SkillCategory.objects.get(user=self.user.id).category,
            'updatecategory'
            )

    def test_skill_category_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'skill_category_update',
            kwargs={'pk_category': self.user.id}
            ),
            {'category': 'updatecategory'})
        self.assertEqual(response.status_code, 302)

    def test_skill_category_delete_view(self):
        response = self.client.get(
            reverse(
                'skill_category_delete',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(0, categories)

    def test_skill_category_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_category_delete',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        categories = SkillCategory.objects.filter(user=self.user).count()
        self.assertEqual(1, categories)

    def test_skill_category_detail_view(self):
        response = self.client.get(
            reverse(
                'skill_category_detail',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_skill_category_detail_view_invalid_pk_category(self):
        response = self.client.get(
            reverse(
                'skill_category_detail',
                kwargs={'pk_category': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_skill_category_detail_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_category_detail',
                kwargs={'pk_category': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_skill_get_view(self):
        response = self.client.get(reverse(
            'skill_new', kwargs={'pk_category': self.skillcategory.id})
            )
        self.assertEqual(response.status_code, 200)

    def test_create_skill_get_view_invalid_pk_category(self):
        response = self.client.get(
            reverse('skill_new', kwargs={'pk_category': 1000})
            )
        self.assertEqual(response.status_code, 302)

    def test_create_skill_post_view(self):
        response = self.client.post(
            reverse(
                'skill_new',
                kwargs={'pk_category': self.skillcategory.id}
                ),
            {'name': 'testname2'}
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(2, skill)

    def test_create_skill_post_view_invalid_pk_category(self):
        response = self.client.post(
            reverse('skill_new', kwargs={'pk_category': 1000}),
            {'name': 'testname2'}
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(1, skill)

    def test_create_skill_get_logout_view(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_new',
                kwargs={'pk_category': self.skillcategory.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_skill_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse(
                'skill_new',
                kwargs={'pk_category': self.skillcategory.id}
                ),
            {'name': 'testname2'}
            )
        self.assertEqual(response.status_code, 302)

    def test_skill_edit_view_get(self):
        response = self.client.get(
            reverse(
                'skill_edit',
                kwargs={
                    'pk_category': self.skillcategory.id,
                    'pk_skill': self.skill.id
                    }
                ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 200)

    def test_skill_category_edit_view_get_invalid_pk_category(self):
        response = self.client.get(
            reverse(
                'skill_edit',
                kwargs={'pk_category': 1000, 'pk_skill': self.skill.id}
                ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)

    def test_skill_category_edit_view_get_invalid_pk_skill(self):
        response = self.client.get(
            reverse(
                'skill_edit',
                kwargs={'pk_category': self.skillcategory.id, 'pk_skill': 1000}
                ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)

    def test_skill_category_edit_view_get_invalid_pk_category_pk_skill(self):
        response = self.client.get(
            reverse(
                'skill_edit',
                kwargs={'pk_category': 1000, 'pk_skill': 1000}
                ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)

    def test_skill_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_edit',
                kwargs={
                    'pk_category': self.skillcategory.id,
                    'pk_skill': self.skill.id
                    }
                ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)

    def test_skill_edit_view_post(self):
        response = self.client.post(reverse(
            'skill_edit',
            kwargs={'pk_category': self.skillcategory.id,
                    'pk_skill': self.skill.id}
                    ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Skill.objects.get(skill_category_id=self.skillcategory.id).name,
            'testnameupdate'
            )

    def test_skill_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'skill_edit',
            kwargs={
                'pk_category': self.skillcategory.id,
                'pk_skill': self.skill.id
                }
            ),
            {'name': 'testnameupdate'})
        self.assertEqual(response.status_code, 302)

    def test_skill_delete_view(self):
        response = self.client.get(
            reverse(
                'skill_delete',
                kwargs={
                    'pk_category': self.skillcategory.id,
                    'pk_skill': self.skill.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(0, skill)

    def test_skill_delete_view_invalid_pk_category(self):
        response = self.client.get(
            reverse(
                'skill_delete',
                kwargs={'pk_category': 1000, 'pk_skill': self.skill.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(1, skill)

    def test_skill_delete_view_invalid_pk_skill(self):
        response = self.client.get(
            reverse(
                'skill_delete',
                kwargs={
                    'pk_category': self.skillcategory.id,
                    'pk_skill': 1000
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(1, skill)

    def test_skill_delete_view_invalid_pk_category_pk_skill(self):
        response = self.client.get(
            reverse(
                'skill_delete',
                kwargs={'pk_category': 1000, 'pk_skill': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(1, skill)

    def test_skill_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'skill_delete',
                kwargs={
                    'pk_category': self.skillcategory.id,
                    'pk_skill': self.skill.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        skill = Skill.objects.filter(
            skill_category_id=self.skillcategory.id
            ).count()
        self.assertEqual(1, skill)
