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
