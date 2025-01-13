from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User
from experiences_app.models import Experience, ExperienceDescription


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
        self.experience = Experience.objects.create(
            user=self.user, title='testtitle',
            role='testrole', start_date='2012-12-12',
            end_date='2013-12-12'
        )
        self.experiencedescription = ExperienceDescription.objects.create(
            experience_id=self.experience.id,
            description='testdescription'
        )

    def test_create_experience_get_view(self):
        response = self.client.get(reverse('experience_new'))
        self.assertEqual(response.status_code, 200)

    def test_create_experience_post_view(self):
        response = self.client.post(
            reverse('experience_new'),
            {'title': 'testtitle2',
             'role': 'testrole2', 'start_date': '2000-01-01',
             'end_date': '2006-06-06'}
            )
        self.assertEqual(response.status_code, 302)
        experience = Experience.objects.filter(user=self.user).count()
        self.assertEqual(2, experience)

    def test_create_experience_get_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('experience_new'))
        self.assertEqual(response.status_code, 302)

    def test_create_experience_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse('experience_new'),
            {'title': 'testtitle2',
             'role': 'testrole2', 'start_date': '2000-01-01',
             'end_date': '2006-06-06'}
            )
        self.assertEqual(response.status_code, 302)

    def test_index_experience_View(self):
        response = self.client.get(reverse('experiences_list'))
        self.assertEqual(response.status_code, 200)

    def test_index_experience_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('experiences_list'))
        self.assertEqual(response.status_code, 302)
        experience = Experience.objects.filter(user=self.user).count()
        self.assertEqual(1, experience)

    def test_experience_edit_view_get(self):
        response = self.client.get(
            reverse(
                'experience_update',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_experience_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_update',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_experience_edit_view_post(self):
        response = self.client.post(reverse(
            'experience_update',
            kwargs={'pk_experience': self.experience.id}
            ),
            {'title': 'updatetesttitle2',
             'role': 'updatetestrole2', 'start_date': '1999-12-12',
             'end_date': '1980-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Experience.objects.get(user=self.user.id).title,
            'updatetesttitle2'
            )
        self.assertEqual(
            Experience.objects.get(user=self.user.id).role,
            'updatetestrole2'
            )
        self.assertEqual(
            Experience.objects.get(
                user=self.user.id
                ).start_date.strftime('%Y-%m-%d'),
            '1999-12-12'
            )
        self.assertEqual(
            Experience.objects.get(
                user=self.user.id
                ).end_date.strftime('%Y-%m-%d'),
            '1980-12-12'
            )

    def test_experience_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'experience_update',
            kwargs={'pk_experience': self.user.id}
            ),
            {'title': 'updatetesttitle2',
             'role': 'updatetestrole2', 'start_date': '1999-07-07',
             'end_date': '1980-04-04'})
        self.assertEqual(response.status_code, 302)

    def test_experience_delete_view(self):
        response = self.client.get(
            reverse(
                'experience_delete',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        experience = Experience.objects.filter(user=self.user).count()
        self.assertEqual(0, experience)

    def test_experience_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_delete',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        experience = Experience.objects.filter(user=self.user).count()
        self.assertEqual(1, experience)

    def test_experience_detail_view(self):
        response = self.client.get(
            reverse(
                'experience_detail',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_experience_detail_view_invalid_pk_experience(self):
        response = self.client.get(
            reverse(
                'experience_detail',
                kwargs={'pk_experience': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_experience_detail_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_detail',
                kwargs={'pk_experience': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_experience_description_get_view(self):
        response = self.client.get(reverse(
            'experience_description_new', kwargs={'pk_experience': self.experience.id})
            )
        self.assertEqual(response.status_code, 200)

    def test_create_experience_description_get_view_invalid_pk_experience(self):
        response = self.client.get(
            reverse('experience_description_new', kwargs={'pk_experience': 1000})
            )
        self.assertEqual(response.status_code, 302)

    def test_create_experience_description_post_view(self):
        response = self.client.post(
            reverse(
                'experience_description_new',
                kwargs={'pk_experience': self.experience.id}
                ),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(2, experiencedescription)

    def test_create_experience_description_post_view_invalid_pk_experience(self):
        response = self.client.post(
            reverse('experience_description_new', kwargs={'pk_experience': 1000}),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(1, experiencedescription)

    def test_create_experience_description_get_logout_view(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_description_new',
                kwargs={'pk_experience': self.experience.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_experience_description_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse(
                'experience_description_new',
                kwargs={'pk_experience': self.experience.id}
                ),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)

    def test_experience_description_edit_view_get(self):
        response = self.client.get(
            reverse(
                'experience_description_edit',
                kwargs={
                    'pk_experience': self.experiencedescription.id,
                    'pk_experience_description': self.experiencedescription.id
                    }
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 200)

    def test_experience_description_edit_view_get_invalid_pk_experience(self):
        response = self.client.get(
            reverse(
                'experience_description_edit',
                kwargs={'pk_experience': 1000, 'pk_experience_description': self.experiencedescription.id}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_experience_description_edit_view_get_invalid_pk_experience_description(self):
        response = self.client.get(
            reverse(
                'experience_description_edit',
                kwargs={'pk_experience': self.experience.id, 'pk_experience_description': 1000}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_experience_description_edit_view_get_invalid_pk_experience_pk_experience_description(self):
        response = self.client.get(
            reverse(
                'experience_description_edit',
                kwargs={'pk_experience': 1000, 'pk_experience_description': 1000}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_experience_description_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_description_edit',
                kwargs={
                    'pk_experience': self.experiencedescription.id,
                    'pk_experience_description': self.experiencedescription.id
                    }
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_experience_description_edit_view_post(self):
        response = self.client.post(reverse(
            'experience_description_edit',
            kwargs={'pk_experience': self.experience.id,
                    'pk_experience_description': self.experiencedescription.id}
                    ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            ExperienceDescription.objects.get(experience_id=self.experience.id).description,
            'updatedescription'
            )

    def test_experience_description_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'experience_description_edit',
            kwargs={
                'pk_experience': self.experiencedescription.id,
                'pk_experience_description': self.experiencedescription.id
                }
            ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_experience_description_delete_view(self):
        response = self.client.get(
            reverse(
                'experience_description_delete',
                kwargs={
                    'pk_experience': self.experiencedescription.id,
                    'pk_experience_description': self.experiencedescription.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(0, experiencedescription)

    def test_experience_description_delete_view_invalid_pk_experience(self):
        response = self.client.get(
            reverse(
                'experience_description_delete',
                kwargs={'pk_experience': 1000, 'pk_experience_description': self.experiencedescription.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(1, experiencedescription)

    def test_experience_description_delete_view_invalid_pk_experience_description(self):
        response = self.client.get(
            reverse(
                'experience_description_delete',
                kwargs={
                    'pk_experience': self.experiencedescription.id,
                    'pk_experience_description': 1000
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(1, experiencedescription)

    def test_experience_description_delete_view_invalid_pk_experience_pk_experience_description(self):
        response = self.client.get(
            reverse(
                'experience_description_delete',
                kwargs={'pk_experience': 1000, 'pk_experience_description': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(1, experiencedescription)

    def test_experience_description_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'experience_description_delete',
                kwargs={
                    'pk_experience': self.experiencedescription.id,
                    'pk_experience_description': self.experiencedescription.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        experiencedescription = ExperienceDescription.objects.filter(
            experience_id=self.experience.id
            ).count()
        self.assertEqual(1, experiencedescription)
