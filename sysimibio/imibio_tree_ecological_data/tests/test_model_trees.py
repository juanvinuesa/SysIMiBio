from django.core.exceptions import ValidationError
from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree


class TreeModelSociologicalTest(TestCase):
    def setUp(self):
        self.field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator="Florencia",
            staff='Felipe',
            parcel_id=1
        )

    def test_sociologicalclassification_Emergente(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Emergente'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Dominante(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Dominante'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Codominante(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Codominante'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Intermedia(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Intermedia'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Inferior_suprimido(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Inferior suprimido'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Inferior_sumergido(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Inferior sumergido'
        )
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_CHOICES(self):
        """"Sociological classification mus be limited by choices"""
        tree = Tree.objects.create(
            field=self.field,
            tree_id=1,
            specie='Solanaceae',
            dap=40,
            dab=60,
            tree_height=60,
            latitude=-26,
            longitude=-54,
            photo='http://www.google.com',
            obs='Teste 1',
            tree_status='Teste estado del arbol',
            phytosanitary_status='Bueno',
            sociological_classification='Bad Sociological Classification'
        )
        self.assertRaises(ValidationError, tree.full_clean)

class TreeModelPhytosanitaryTest(TestCase):
    def setUp(self):
        self.field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator="Florencia",
            staff='Felipe',
            parcel_id=1
        )

    def test_phytosanitary_Bueno(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Bueno',
            sociological_classification='Emergente'
        )
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Regular(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Regular',
            sociological_classification='Dominante'
        )
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Malo(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Malo',
            sociological_classification='Codominante'
        )
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Muerto(self):
        tree = Tree.objects.create(
            field=self.field,
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
            phytosanitary_status='Muerto',
            sociological_classification='Intermedia'
        )
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_CHOICES(self):
        """"Sociological classification mus be limited by choices"""
        tree = Tree.objects.create(
            field=self.field,
            tree_id=1,
            specie='Solanaceae',
            dap=40,
            dab=60,
            tree_height=60,
            latitude=-26,
            longitude=-54,
            photo='http://www.google.com',
            obs='Teste 1',
            tree_status='Teste estado del arbol',
            phytosanitary_status='BAD phytosanitary',
            sociological_classification='Emergente'
        )
        self.assertRaises(ValidationError, tree.full_clean)
