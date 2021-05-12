from django.test import TestCase

import geojson
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from geojson import Polygon, Point

from sysimibio.imibio_tree_ecological_data.forms import PermanentParcelForm

class PermanenParcelFormTest(TestCase):
    def setUp(self):
        self.pp = PermanentParcelForm()

    def test_permanent_parcel_has_fields(self):
        """Permanent Parcel form must have models fields"""
        self.assertSequenceEqual(
            ['name', 'province', 'municipality', 'locality', 'obs', 'latitude', 'longitude',
             'geom'], list(self.pp.fields))

    def make_PPForm_validated(self, **kwargs):
        valid = dict(name="YryaPu",
            province='Misiones', municipality='Capital',
            locality='600Ha', obs='Parcela de prueba', latitude=-26,
                     longitude=-54, geom=Polygon([[(-54.6,-27.0), (-54.0, -27.07), (-54.07,-26.62), (-54.6,-27.0)]]))
        data = dict(valid, **kwargs)
        form = PermanentParcelForm(data)
        # form.is_valid()
        return form

    def test_form_is_valid(self):
        form = self.make_PPForm_validated()
        form = form.is_valid()
        self.assertTrue(form)

    def test_province_restriction(self):
        """"province different from Misiones must return error"""
        form = self.make_PPForm_validated(province="OtraProvincia")
        form = form.is_valid()
        self.assertFalse(form)

    def test_geom_is_invalid(self):
        """"geom must be polygon geojson"""
        form = self.make_PPForm_validated(geom=Point((-54.6,-27.0)))
        form.is_valid()
        self.assertEquals(form.errors["geom"][0], "Point does not Match geometry type")
