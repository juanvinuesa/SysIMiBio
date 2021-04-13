from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import resolve_url as r
from sysimibio.imibio_tree_ecological_data.forms import FieldForm, TreeForm
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeRegistrationFormTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('imibio_tree_ecological_data:new'))
        self.Treeform = TreeForm()
        self.Fieldform = FieldForm()
        self.coordinator1 = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.staff1 = User.objects.create_user('Felipe', 'feli@imibio.com', 'felipassword')
        self.field1 = TreeEcologicalData.objects.create(date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator1,
            parcel_id=1)

    def test_Fieldform_has_fields(self):
        """Field form must have models fields"""
        self.assertSequenceEqual(
            ['date', 'start_time', 'end_time', 'temperature',
             'humidity', 'coordinator', 'staff', 'parcel_id'], list(self.Fieldform.fields))

    def test_Treeform_has_fields(self):
        """Tree form must have models fields"""
        self.assertSequenceEqual(
            ['field', 'tree_id', 'specie', 'dap', 'dab', 'tree_height', 'latitude',
             'longitude', 'picture', 'obs',
             'phytosanitary_status', 'sociological_classification'], list(self.Treeform.fields))

    def make_FieldForm_validated(self, **kwargs):
        valid = dict(date='2020-12-01',
            start_time='0:0',
            end_time='0:30', temperature=35.9,
            humidity=80, coordinator=self.coordinator1,
            staff=[self.staff1],
            parcel_id=1)

        data = dict(valid, **kwargs)
        form = FieldForm(data)
        form.is_valid()
        return form

    def make_TreeForm_validated(self, **kwargs):
        valid = dict(field=self.field1,
            tree_id=1, specie='Solanaceae',
            dap=40, dab=60, tree_height=60, latitude=-26, longitude=-54,
            # picture = 'www.google.com',
            obs='Teste 1',
            phytosanitary_status='Muerto', sociological_classification='Emergente')
        data = dict(valid, **kwargs)
        form = TreeForm(data)
        form.is_valid()
        return form

    def assertFormCode(self, form, field, code):
        error = form.errors.as_data()
        error_list = error[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def test_start_time_not_bigger_than_end_time(self):
        """Start time must be lower then end time"""
        form = self.make_FieldForm_validated(start_time='10:40', end_time='9:00')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_date_not_bigger_then_today(self):
        form = self.make_FieldForm_validated(date='2050-12-31')
        self.assertFormCode(form, 'date', 'Date in the future')

    def test_temp_not_bigger_45(self):
        form = self.make_FieldForm_validated(temperature='46')
        self.assertFormCode(form, 'temperature', 'Temperature out of the range')

    def test_temp_not_lower_minus5(self):
        form = self.make_FieldForm_validated(temperature='-6')
        self.assertFormCode(form, 'temperature', 'Temperature out of the range')

    def test_humedad_not_bigger_100(self):
        form = self.make_FieldForm_validated(humidity='101')
        self.assertFormCode(form, 'humidity', 'Humidity out of the range')

    def test_humedad_not_lower_0(self):
        form = self.make_FieldForm_validated(humidity='-1')
        self.assertFormCode(form, 'humidity', 'Humidity out of the range')

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
