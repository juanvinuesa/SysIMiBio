from django.test import TestCase
from sysimibio.imibio_ecological_data.forms import TreeEcologicalForm
from sysimibio.imibio_ecological_data.models import TreeEcologicalData


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
            ('<input', 22),
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


class TreeEcologicalDataRegistrationPostValid(TestCase):
    def setUp(self):
        self.data = dict(
            fecha='01/01/01',
            hora_inicio='0:0',
            hora_final='0:30',
            temperatura=35.9,
            humedad=80,
            responsable="Florencia",
            acompanantes="Felipe",
            id_parcela=1,
            id_arbol=1,
            especie='Solanaceae',
            dap=40,
            dab=60,
            altura=60,
            latitud=-43,
            longitud=-56,
            fotografia=True,
            obs='Teste 1',
            estado_arbol='Teste estado del arbol',
            forma_vida='Estado de vida',
            clasificacion_sociologica='Clasificacion de vida')
        self.resp = self.client.post('/registro_ecologico_arboreas/', self.data)

    def test_Post(self):
        """Valid post should redirect"""
        self.assertEqual(302, self.resp.status_code)

    def test_save_TreeEcologicalRegistration(self):
        self.assertTrue(TreeEcologicalData.objects.exists())


class TreeEcologicalDataRegistrationPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/registro_ecologico_arboreas/', {})
        self.form = self.resp.context['form']

    def test_Post(self):
        """Invalid post must not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'tree_ecological_registration_form.html')

    def test_template_has_form(self):
        self.assertIsInstance(self.form, TreeEcologicalForm)

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)

    def test_dont_save_TreeEcologicalRegistration(self):
        self.assertFalse(TreeEcologicalData.objects.exists())
