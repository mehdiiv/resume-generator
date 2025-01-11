from django.test import TestCase
from skill.models import SkillCategory, Skill
from user_app.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='test', last_name='testlast',
            email='test@test.com', password='testpassword',
            github_link='https://github.com/',
            linkedin_link='https://linkedinlink.com/',
            phone_number='+912555464',
            country='iran',
            city='tehran',
            about_me='sdsdadadasdasdasdasdasda',
            image=''
            )

        self.skillcategoty = SkillCategory.objects.create(
            user_id=self.user.id, category='zzzzzzzzzz'
        )
        self.skill = Skill.objects.create(
            skill_category_id=self.user.id, name='testname'
        )

    def test_model_skillcategory_cerate(self):
        self.assertEqual(self.skillcategoty.category, 'zzzzzzzzzz')

    def test_model_skillcategory_name(self):
        self.assertEqual(self.skillcategoty._meta.db_table, 'skill_categories')

    def test_model_skill_cerate(self):
        self.assertEqual(self.skill.name, 'testname')

    def test_model_skill_name(self):
        self.assertEqual(self.skill._meta.db_table, 'skills')
