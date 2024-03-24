from django.test import TestCase


class TestPostListViews(TestCase):
    def test_get_post_list_page(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')
