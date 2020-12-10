from django.test import TestCase
from django.shortcuts import resolve_url as r
from datetime import date, time
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeEcologicalRegistrationDetailGet(TestCase):
    def setUp(self):
        self.obj = TreeEcologicalData.objects.create(
            fecha=date(2020,12,30),
            hora_inicio=time(0),
            hora_final=time(0,30),
            temperatura=35.9,
            humedad=80,
            responsable="Florencia",
            acompanantes='Felipe',
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
            self.obj.fecha,#date(2020,12,30),
            # time(0),
            # time(0,30),
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
            True,
            'Teste 1',
            'Teste estado del arbol',
            'Estado de vida',
            'Clasificacion de vida')
        with self.subTest():
            for expected in content:
                self.assertContains(self.resp, expected)

class TreeEcologicalRegistrationDetailGet(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('imibio_tree_ecological_data:detail', 0))
        self.assertEqual(404, resp.status_code)
