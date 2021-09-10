import geojson
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase

from sysimibio.imibio_tree_ecological_data.forms import FieldForm, TreeForm
from sysimibio.imibio_tree_ecological_data.models import FieldWork, PermanentParcel


class TreeRegistrationFormTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('imibio_tree_ecological_data:tree_create'))
        self.Treeform = TreeForm()
        self.Fieldform = FieldForm()
        self.coordinator1 = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=self.coordinator1,
                                                      province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha', obs='Observacion', latitude=-26, longitude=-56,
                                                      geom='')
        self.staff1 = User.objects.create_user('Felipe', 'feli@imibio.com', 'felipassword')
        self.field1 = FieldWork.objects.create(date='2020-12-30',
                                               start_time='0:0',
                                               end_time='0:30',
                                               temperature=35.9,
                                               humidity=80,
                                               coordinator=self.coordinator1,
                                               parcel_id=self.parcel1)

    def test_Treeform_has_fields(self):
        """Tree form must have models fields"""
        self.assertSequenceEqual(
            ['field', 'subplot', 'tree_number', 'specie', 'latitude',
             'longitude',
             # 'picture', # todo remove
             'obs', 'geom'], list(self.Treeform.fields))

    def make_TreeForm_validated(self, **kwargs):
        valid = dict(field=self.field1,
                     subplot='A1',
                     tree_number=1,
                     specie='Solanaceae',
                     latitude=-26, longitude=-54,
                     obs='Teste 1')
        data = dict(valid, **kwargs)
        form = TreeForm(data)
        form.is_valid()
        return form

    def assertFormCode(self, form, field, code):
        error = form.errors.as_data()
        error_list = error[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def test_min_latitud_value(self):
        form = self.make_TreeForm_validated(latitude='-28.18')
        self.assertFormCode(form, 'latitude', 'Latitude out of the range')

    def test_max_latitud_value(self):
        form = self.make_TreeForm_validated(latitude='-25.47')
        self.assertFormCode(form, 'latitude', 'Latitude out of the range')

    def test_min_longitud_value(self):
        form = self.make_TreeForm_validated(longitude='-56.07')
        self.assertFormCode(form, 'longitude', 'Longitude out of the range')

    def test_max_longitud_value(self):
        form = self.make_TreeForm_validated(longitude='-53.61')
        self.assertFormCode(form, 'longitude', 'Longitude out of the range')

    def test_form_is_valid(self):
        form = self.make_TreeForm_validated()
        form = form.is_valid()
        self.assertTrue(form)

    def test_geom_is_geojson_istance(self):
        form = self.make_TreeForm_validated()
        self.assertIsInstance(form.cleaned_data.get('geom'), (geojson.geometry.Point,))
