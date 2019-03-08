from django.test import TestCase


class ProductListTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/products/')
        self.assertEqual(resp.status_code, 200)
