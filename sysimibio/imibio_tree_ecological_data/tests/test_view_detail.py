from django.test import TestCase
from django.shortcuts import resolve_url as r
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeEcologicalRegistrationDetailGet(TestCase):
    def setUp(self):
        self.obj = TreeEcologicalData.objects.create(
            date='2020-12-31',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            cordinator="Florencia",
            staff='Felipe',
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
        self.resp = self.client.get(r('imibio_tree_ecological_data:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'tree_ecological_detail.html')

    def test_context(self):
        tree_detail = self.resp.context['tree_detail']
        self.assertIsInstance(tree_detail, TreeEcologicalData)

    def test_html(self):
        content = (
            '2020-12-31',
            '0:0',
            '0:30',
            35.9,
            80,
            "Florencia",
            'Felipe',
            1,
            1,
            'Solanaceae',
            40,
            60,
            60,
            -43,
            -56,
            'www.google.com',
            'Teste 1',
            'Teste estado del arbol',
            'Estado de vida',
            'Clasificacion de vida')
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

class TreeEcologicalRegistrationDetailGet(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('imibio_tree_ecological_data:detail', 0))
        self.assertEqual(404, resp.status_code)
