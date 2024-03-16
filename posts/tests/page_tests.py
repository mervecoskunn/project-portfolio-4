from django.contrib.auth import get_user_model
from django.test import TestCase


class TestPostListViews(TestCase):
    def test_get_post_list_page(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')


class TestUserPageViews(TestCase):
    def test_profile_page(self):
        user = get_user_model()
        user = user.objects.create_user(username="testuser", password="secret")
        response = self.client.get(f'/user/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/user_page.html')
