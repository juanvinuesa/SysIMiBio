from django.test import TestCase
from sysimibio.imibio_occurrences.forms import OccurrencesRegistrationForm

class RegistrationsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("/registro_ocurrencias/")

    def test_get(self):
        """get /registro_ocurrencias/ must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """must use imibio_occurrences/occurrences_registration_form.html"""
        self.assertTemplateUsed(self.resp, 'occurrences/occurrences_registration_form.html')

    def test_html(self):
        """HTML must contais input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have occurrence registration form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, OccurrencesRegistrationForm)

    def test_form_has_fields(self):
        """Form must have 19 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual([
        'basisOfRecord',
        'institutionCode',
        'collectionCode',
        'catalogNumber',
        'scientificName',
        'kingdom',
        'phylum',
        'clase',
        'order',
        'family',
        'genus',
        'specificEpithet',
        'taxonRank',
        'infraspecificEpithet',
        'identificationQualifier',
        'county',
        'stateProvince',
        'locality',
        'recordedBy',
        'recordNumber',
        'decimalLatitude',
        'decimalLongitude'], list(form.fields))