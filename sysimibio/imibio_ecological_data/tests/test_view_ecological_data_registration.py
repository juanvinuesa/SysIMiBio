from django.test import TestCase
from sysimibio.imibio_ecological_data.forms import TreeEcologicalForm

class TreeEcologicalRegistrationGet(TestCase):
    def setUp(self):
        self.resp = self.client.get("/registro_ecologico_arboreas/")

    def test_get(self):
        """GET /registro_ecologico/ must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_use_template(self):
        """must use ecological_registration.html template"""
        self.assertTemplateUsed(self.resp, 'tree_ecological_registration_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        tags = (
            ('<form', 2),
            ('<input', 20),
            ('type="submit"', 2))
        for text, amount in tags:
            with self.subTest():
                self.assertContains(self.resp, text, amount)

    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context must have tree ecological data registration form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, TreeEcologicalForm)

    def test_form_has_fields(self):
        """form must have 21 fields"""
        form = self.resp.context['form']
        self.assertEqual(
            ['fecha', 'hora_inicio', 'hora_final', 'temperatura', 'humedad', 'responsable', 'acompanante',
             'id_arbol', 'especie', 'dap', 'dab', 'altura', 'latitud', 'longitud', 'fotografia', 'obs', 'estado_arbol',
             'forma_vida', 'clasificacion_sociologica'],
        list(form.fields))