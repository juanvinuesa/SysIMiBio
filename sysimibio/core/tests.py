from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        """creating response instance atribute"""
        self.response = self.client.get('/')

    def test_get(self):
        "GET must return status 200"
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        "Must use index.html"
        self.assertTemplateUsed(self.response, 'index.html')
