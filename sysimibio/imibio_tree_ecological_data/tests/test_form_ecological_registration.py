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
            dap = 40, dab = 60, altura = 60, latitud = -43, longitud = -56,
            fotografia = True, obs = 'Teste 1', estado_arbol = 'Teste estado del arbol',
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
