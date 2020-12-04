from datetime import datetime

from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeEcologicalRegistrationTest(TestCase):
    def setUp(self):
        self.obj = TreeEcologicalData(
            fecha='2020-12-30',
            hora_inicio='0:0',
            hora_final='0:30',
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
        self.obj.save()

    def test_create(self):
        self.assertTrue(TreeEcologicalData.objects.exists())

    def test_created_at(self):
        """ecological registration must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
