from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User
from educations_app.models import Education, EducationDescription


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
        self.education = Education.objects.create(
            user=self.user, university='testuniversity',
            level='testlevel', start_date='2012-12-12',
            end_date='2013-12-12', field='testfield',
        )
        self.educationdescription = EducationDescription.objects.create(
            education_id=self.education.id,
            description='testdescription'
        )

    def test_create_education_get_view(self):
        response = self.client.get(reverse('education_new'))
        self.assertEqual(response.status_code, 200)

    def test_create_education_post_view(self):
        response = self.client.post(
            reverse('education_new'),
            {'university': 'testuniversity2', 'field': 'testfield',
             'level': 'testlevel2', 'start_date': '2000-01-01',
             'end_date': '2006-06-06'}
            )
        self.assertEqual(response.status_code, 302)
        education = Education.objects.filter(user=self.user).count()
        self.assertEqual(2, education)

    def test_create_education_get_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('education_new'))
        self.assertEqual(response.status_code, 302)

    def test_create_education_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse('education_new'),
            {'university': 'testuniversity2', 'field': 'testfield',
             'level': 'testlevel2', 'start_date': '2000-01-01',
             'end_date': '2006-06-06'}
            )
        self.assertEqual(response.status_code, 302)

    def test_index_education_View(self):
        response = self.client.get(reverse('educations_list'))
        self.assertEqual(response.status_code, 200)

    def test_index_education_logout_view(self):
        logout(self.client)
        response = self.client.get(reverse('educations_list'))
        self.assertEqual(response.status_code, 302)
        education = Education.objects.filter(user=self.user).count()
        self.assertEqual(1, education)

    def test_education_edit_view_get(self):
        response = self.client.get(
            reverse(
                'education_update',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_education_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_update',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_education_edit_view_post(self):
        response = self.client.post(reverse(
            'education_update',
            kwargs={'pk_education': self.education.id}
            ),
            {'university': 'updatetestuniversity2', 'field': 'testfield',
             'level': 'updatetestlevel2', 'start_date': '1999-12-12',
             'end_date': '1980-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Education.objects.get(user=self.user.id).university,
            'updatetestuniversity2'
            )
        self.assertEqual(
            Education.objects.get(user=self.user.id).level,
            'updatetestlevel2'
            )
        self.assertEqual(
            Education.objects.get(
                user=self.user.id
                ).start_date.strftime('%Y-%m-%d'),
            '1999-12-12'
            )
        self.assertEqual(
            Education.objects.get(
                user=self.user.id
                ).end_date.strftime('%Y-%m-%d'),
            '1980-12-12'
            )

    def test_education_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'education_update',
            kwargs={'pk_education': self.user.id}
            ),
            {'university': 'updatetestuniversity2', 'field': 'testfield',
             'level': 'updatetestlevel2', 'start_date': '1999-07-07',
             'end_date': '1980-04-04'})
        self.assertEqual(response.status_code, 302)

    def test_education_delete_view(self):
        response = self.client.get(
            reverse(
                'education_delete',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        education = Education.objects.filter(user=self.user).count()
        self.assertEqual(0, education)

    def test_education_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_delete',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        education = Education.objects.filter(user=self.user).count()
        self.assertEqual(1, education)

    def test_education_detail_view(self):
        response = self.client.get(
            reverse(
                'education_detail',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 200)

    def test_education_detail_view_invalid_pk_education(self):
        response = self.client.get(
            reverse(
                'education_detail',
                kwargs={'pk_education': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_education_detail_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_detail',
                kwargs={'pk_education': self.user.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_education_description_get_view(self):
        response = self.client.get(reverse(
            'education_description_new', kwargs={'pk_education': self.education.id})
            )
        self.assertEqual(response.status_code, 200)

    def test_create_education_description_get_view_invalid_pk_education(self):
        response = self.client.get(
            reverse('education_description_new', kwargs={'pk_education': 1000})
            )
        self.assertEqual(response.status_code, 302)

    def test_create_education_description_post_view(self):
        response = self.client.post(
            reverse(
                'education_description_new',
                kwargs={'pk_education': self.education.id}
                ),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(2, educationdescription)

    def test_create_education_description_post_view_invalid_pk_education(self):
        response = self.client.post(
            reverse('education_description_new', kwargs={'pk_education': 1000}),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(1, educationdescription)

    def test_create_education_description_get_logout_view(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_description_new',
                kwargs={'pk_education': self.education.id}
                )
            )
        self.assertEqual(response.status_code, 302)

    def test_create_education_description_post_logout_view(self):
        logout(self.client)
        response = self.client.post(
            reverse(
                'education_description_new',
                kwargs={'pk_education': self.education.id}
                ),
            {'description': 'testdescription2'}
            )
        self.assertEqual(response.status_code, 302)

    def test_education_description_edit_view_get(self):
        response = self.client.get(
            reverse(
                'education_description_edit',
                kwargs={
                    'pk_education': self.educationdescription.id,
                    'pk_education_description': self.educationdescription.id
                    }
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 200)

    def test_education_description_edit_view_get_invalid_pk_education(self):
        response = self.client.get(
            reverse(
                'education_description_edit',
                kwargs={'pk_education': 1000, 'pk_education_description': self.educationdescription.id}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_education_description_edit_view_get_invalid_pk_education_description(self):
        response = self.client.get(
            reverse(
                'education_description_edit',
                kwargs={'pk_education': self.education.id, 'pk_education_description': 1000}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_education_description_edit_view_get_invalid_pk_education_pk_education_description(self):
        response = self.client.get(
            reverse(
                'education_description_edit',
                kwargs={'pk_education': 1000, 'pk_education_description': 1000}
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_education_description_edit_view_get_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_description_edit',
                kwargs={
                    'pk_education': self.educationdescription.id,
                    'pk_education_description': self.educationdescription.id
                    }
                ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_education_description_edit_view_post(self):
        response = self.client.post(reverse(
            'education_description_edit',
            kwargs={'pk_education': self.education.id,
                    'pk_education_description': self.educationdescription.id}
                    ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            EducationDescription.objects.get(education_id=self.education.id).description,
            'updatedescription'
            )

    def test_education_description_edit_view_post_logout(self):
        logout(self.client)
        response = self.client.post(reverse(
            'education_description_edit',
            kwargs={
                'pk_education': self.educationdescription.id,
                'pk_education_description': self.educationdescription.id
                }
            ),
            {'description': 'updatedescription'})
        self.assertEqual(response.status_code, 302)

    def test_education_description_delete_view(self):
        response = self.client.get(
            reverse(
                'education_description_delete',
                kwargs={
                    'pk_education': self.educationdescription.id,
                    'pk_education_description': self.educationdescription.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(0, educationdescription)

    def test_education_description_delete_view_invalid_pk_education(self):
        response = self.client.get(
            reverse(
                'education_description_delete',
                kwargs={'pk_education': 1000, 'pk_education_description': self.educationdescription.id}
                )
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(1, educationdescription)

    def test_education_description_delete_view_invalid_pk_education_description(self):
        response = self.client.get(
            reverse(
                'education_description_delete',
                kwargs={
                    'pk_education': self.educationdescription.id,
                    'pk_education_description': 1000
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(1, educationdescription)

    def test_education_description_delete_view_invalid_pk_education_pk_education_description(self):
        response = self.client.get(
            reverse(
                'education_description_delete',
                kwargs={'pk_education': 1000, 'pk_education_description': 1000}
                )
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(1, educationdescription)

    def test_education_description_delete_view_logout(self):
        logout(self.client)
        response = self.client.get(
            reverse(
                'education_description_delete',
                kwargs={
                    'pk_education': self.educationdescription.id,
                    'pk_education_description': self.educationdescription.id
                    }
                )
            )
        self.assertEqual(response.status_code, 302)
        educationdescription = EducationDescription.objects.filter(
            education_id=self.education.id
            ).count()
        self.assertEqual(1, educationdescription)
