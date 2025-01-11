from django.test import TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from user_app.models import User
from experiences_app.models import Experience


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
        self.assertEqual(response.status_code, 200)
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
