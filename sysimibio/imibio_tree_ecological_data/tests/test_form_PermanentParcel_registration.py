from django.test import TestCase
from geojson import Polygon, Point

from sysimibio.imibio_tree_ecological_data.forms import PermanentParcelForm

# todo test validators. ver test_form_fieldRegistration
class PermanenParcelFormTest(TestCase):
    def setUp(self):
        self.pp = PermanentParcelForm()

    @staticmethod
    def create_PermanentParcelForm(**kwargs):
        valid_form = dict(
            name="YryaPu",
            province='Misiones', municipality='Capital',
            locality='600Ha', obs='Parcela de prueba', latitude=-26,
            longitude=-54,
            geom=Polygon([[(-54.6, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-54.6, -27.0)]]))
        valid_form.update(**kwargs)
        form = PermanentParcelForm(valid_form)
        return form

    def test_permanent_parcel_has_fields(self):
        """Permanent Parcel form must have models fields"""
        self.assertSequenceEqual(
            ['name', 'province', 'municipality', 'locality', 'obs', 'latitude', 'longitude',
             'geom'], list(self.pp.fields))

    def test_form_is_valid(self):
        form = self.create_PermanentParcelForm()
        self.assertTrue(form.is_valid())

    def test_province_restriction(self):
        """"province different from Misiones must return error"""
        form = self.create_PermanentParcelForm(province="OtraProvincia")
        self.assertFalse(form.is_valid())

    def test_geom_is_invalid(self):
        """"geom must be polygon geojson"""
        form = self.create_PermanentParcelForm(geom=Point((-54.6, -27.0)))
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors["geom"][0], "Point does not match geometry type")
