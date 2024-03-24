from django.test import TestCase


class HomePageTestCase(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
