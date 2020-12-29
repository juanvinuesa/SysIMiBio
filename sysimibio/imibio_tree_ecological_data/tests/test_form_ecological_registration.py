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
            ['fecha', 'hora_inicio', 'hora_final', 'temperatura',
             'humedad', 'responsable', 'acompanantes', 'id_parcela',
             'id_arbol', 'especie', 'dap', 'dab', 'altura', 'latitud',
             'longitud', 'fotografia', 'obs', 'estado_arbol',
             'forma_vida', 'clasificacion_sociologica'], list(self.form.fields))

    def make_validated_form(self, **kwargs):
        valid = dict(fecha = '2020-12-01', hora_inicio = '0:0',
            hora_final = '0:30', temperatura = 35.9,
            humedad = 80, responsable = "Florencia",
            acompanantes = 'Felipe', id_parcela = 1,
            id_arbol = 1, especie = 'Solanaceae',
            dap = 40, dab = 60, altura = 60, latitud = -26, longitud = -54,
            fotografia = 'www.google.com', obs = 'Teste 1', estado_arbol = 'Teste estado del arbol',
            forma_vida = 'Estado de vida', clasificacion_sociologica = 'Clasificacion de vida')
        data = dict(valid, **kwargs)
        form = TreeEcologicalForm(data)
        form.is_valid()
        return form

    def test_start_time_not_bigger_than_end_time(self):
        """Star time must be lower then end time"""
        form = self.make_validated_form(hora_inicio = '0:10', hora_final = '0:0')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_date_not_bigger_then_today(self):
        form = self.make_validated_form(fecha = '2050-12-31')
        self.assertListEqual(['fecha'], list(form.errors))

    def test_temp_not_bigger_45(self):
        form = self.make_validated_form(temperatura = '46')
        self.assertListEqual(['temperatura'], list(form.errors))

    def test_temp_not_lower_minus5(self):
        form = self.make_validated_form(temperatura = '-6')
        self.assertListEqual(['temperatura'], list(form.errors))

    def test_humedad_not_bigger_100(self):
        form = self.make_validated_form(humedad = '101')
        self.assertListEqual(['humedad'], list(form.errors))

    def test_humedad_not_lower_0(self):
        form = self.make_validated_form(humedad = '-1')
        self.assertListEqual(['humedad'], list(form.errors))

    def test_min_latitud_value(self):
        form = self.make_validated_form(latitud = '-28.18')
        self.assertListEqual(['latitud'], list(form.errors))

    def test_max_latitud_value(self):
        form = self.make_validated_form(latitud = '-25.47')
        self.assertListEqual(['latitud'], list(form.errors))

    def test_min_longitud_value(self):
        form = self.make_validated_form(longitud = '-56.07')
        self.assertListEqual(['longitud'], list(form.errors))

    def test_max_longitud_value(self):
        form = self.make_validated_form(longitud = '-53.61')
        self.assertListEqual(['longitud'], list(form.errors))
