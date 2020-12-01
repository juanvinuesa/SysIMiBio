from django.test import TestCase
from sysimibio.imibio_ecological_data.forms import TreeEcologicalForm


class TreeRegistrationFormTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("/registro_ecologico_arboreas/")
        self.form = TreeEcologicalForm()

    def test_form_has_fields(self):
        """form must have 21 fields"""

        self.assertSequenceEqual(
            ['fecha', 'hora_inicio', 'hora_final', 'temperatura',
             'humedad', 'responsable', 'acompanantes', 'id_parcela',
             'id_arbol', 'especie', 'dap', 'dab', 'altura', 'latitud',
             'longitud', 'fotografia', 'obs', 'estado_arbol',
             'forma_vida', 'clasificacion_sociologica'], list(self.form.fields))
