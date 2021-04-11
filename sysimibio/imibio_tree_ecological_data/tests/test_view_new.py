from unittest import skip

from django.test import TestCase
from django.shortcuts import resolve_url as r
# from sysimibio.imibio_tree_ecological_data.forms import TreeEcologicalForm
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


@skip
class TreeEcologicalRegistrationNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('imibio_tree_ecological_data:new'))

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
        self.assertIsInstance(form, TreeEcologicalForm)  # todo resolver esse teste


@skip
class TreeEcologicalDataRegistrationNewPostValid(TestCase):
    def setUp(self):
        self.data = dict(
            date='01/01/01',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator="Florencia",
            staff="Felipe",
            parcel_id=1,
            tree_id=1,
            specie='Solanaceae',
            dap=40,
            dab=60,
            tree_height=60,
            latitude=-26,
            longitude=-54,
            photo='www.google.com',
            obs='Teste 1',
            tree_status='Teste estado del arbol',
            life_form='Estado de vida',
            sociological_classification='Clasificacion de vida')
        self.resp = self.client.post(r('imibio_tree_ecological_data:new'), self.data)

    def test_Post(self):
        """Valid post should redirect to registro_ecologico_arboreas/1/"""
        self.assertRedirects(self.resp, r('imibio_tree_ecological_data:detail', 1))

    def test_save_TreeEcologicalRegistration(self):
        self.assertTrue(TreeEcologicalData.objects.exists())


@skip
class TreeEcologicalDataRegistrationPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('imibio_tree_ecological_data:new'), {})
        self.form = self.resp.context['form']

    def test_Post(self):
        """Invalid post must not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'tree_ecological_registration_form.html')

    def test_template_has_form(self):
        self.assertIsInstance(self.form, TreeEcologicalForm)  # todo resolver esse teste

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)

    def test_dont_save_TreeEcologicalRegistration(self):
        self.assertFalse(TreeEcologicalData.objects.exists())


class TemplateRegressionTest(TestCase):
    def tes_template_has_non_field_errors(self):
        invalid_data = dict(date='2020-12-30', start_time='0:40',
            end_time='0:00', temperature=35.9,
            humidity=80, coordinator="Florencia",
            staff='Felipe', parcel_id=1,
            tree_id=1, specie='Solanaceae',
            dap=40, dab=60, tree_height=60, latitude=-43, longitude=-56,
            photo=True, obs='Teste 1', tree_status='Teste estado del arbol',
            life_form='Estado de vida', sociological_classification='Clasificacion sociologica')
        response = self.client.post(r('imibio_tree_ecological_data:new', invalid_data))

        self.assertContais(response, '<ul class="errorlist nonfield">')
