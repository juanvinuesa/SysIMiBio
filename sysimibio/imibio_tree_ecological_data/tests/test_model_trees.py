from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree


class TreeModelTest(TestCase):
    def test_create(self):
        field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator="Florencia",
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
            sociological_classification='Clasificacion Sociologica'
        )
        tree = Tree.objects.create(
            field=field,
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
            sociological_classification='Clasificacion Sociologica'
        )
        self.assertTrue(Tree.objects.exists())