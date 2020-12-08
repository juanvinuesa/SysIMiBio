from django.test import TestCase
from django.shortcuts import resolve_url as r

class OccurrenceDetailGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/registro_ocurrencias/1/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'occurrences/occurrence_detail.html')