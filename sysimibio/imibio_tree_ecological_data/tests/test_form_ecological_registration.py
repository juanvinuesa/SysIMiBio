from django.test import TestCase
from django.shortcuts import resolve_url as r
from sysimibio.imibio_tree_ecological_data.forms import TreeEcologicalForm


class TreeRegistrationFormTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('imibio_tree_ecological_data:new'))
        self.form = TreeEcologicalForm()

    def test_form_has_fields(self):
        """form must have 21 fields"""

        self.assertSequenceEqual(
            ['date', 'start_time', 'end_time', 'temperature',
             'humidity', 'coordinator', 'staff', 'parcel_id',
             'tree_id', 'specie', 'dap', 'dab', 'tree_height', 'latitude',
             'longitude', 'picture', 'obs',
             'phytosanitary_status', 'sociological_classification'], list(self.form.fields))

    def make_validated_form(self, **kwargs):
        valid = dict(date = '2020-12-01',
                     start_time = '0:0',
            end_time = '0:30', temperature = 35.9,
            humidity = 80, coordinator = "Florencia",
            staff = 'Felipe', parcel_id = 1,
            tree_id = 1, specie = 'Solanaceae',
            dap = 40, dab = 60, tree_height = 60, latitude = -26, longitude = -54,
            # picture = 'www.google.com',
                     obs = 'Teste 1',
            phytosanitary_status = 'Muerto', sociological_classification = 'Emergente')
        data = dict(valid, **kwargs)
        form = TreeEcologicalForm(data)
        form.is_valid()
        return form

    def test_start_time_not_bigger_than_end_time(self):
        """Star time must be lower then end time"""
        form = self.make_validated_form(start_time = '0:40', end_time = '0:00')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_date_not_bigger_then_today(self):
        form = self.make_validated_form(date = '2050-12-31')
        self.assertListEqual(['date'], list(form.errors))

    def test_temp_not_bigger_45(self):
        form = self.make_validated_form(temperature = '46')
        self.assertListEqual(['temperature'], list(form.errors))

    def test_temp_not_lower_minus5(self):
        form = self.make_validated_form(temperature = '-6')
        self.assertListEqual(['temperature'], list(form.errors))

    def test_humedad_not_bigger_100(self):
        form = self.make_validated_form(humidity = '101')
        self.assertListEqual(['humidity'], list(form.errors))

    def test_humedad_not_lower_0(self):
        form = self.make_validated_form(humidity = '-1')
        self.assertListEqual(['humidity'], list(form.errors))

    def test_min_latitud_value(self):
        form = self.make_validated_form(latitude = '-28.18')
        self.assertListEqual(['latitude'], list(form.errors))

    def test_max_latitud_value(self):
        form = self.make_validated_form(latitude = '-25.47')
        self.assertListEqual(['latitude'], list(form.errors))

    def test_min_longitud_value(self):
        form = self.make_validated_form(longitude = '-56.07')
        self.assertListEqual(['longitude'], list(form.errors))

    def test_max_longitud_value(self):
        form = self.make_validated_form(longitude = '-53.61')
        self.assertListEqual(['longitude'], list(form.errors))
