from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree, Pictures
from django.contrib.auth.models import User
# todo refactor tests to have only one dict object

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TreeModelSociologicalTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')

        self.field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=1
        )

        self.valid = Tree(field=self.field,
                     tree_id=1,
                     specie='Solanaceae',
                     dap=40,
                     dab=60,
                     tree_height=60,
                     latitude=-26,
                     longitude=-54,
                     picture=self.tempPicture,
                     obs='Teste 1',
                     phytosanitary_status='Bueno',
                     sociological_classification='Emergente')

    def test_sociologicalclassification_Emergente(self):
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Dominante(self):
        self.valid.sociological_classification = 'Dominante'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Codominante(self):
        self.valid.sociological_classification = 'Codominante'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Intermedia(self):
        self.valid.sociological_classification = 'Intermedia'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Inferior_suprimido(self):
        self.valid.sociological_classification = 'Inferior suprimido'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_Inferior_sumergido(self):
        self.valid.sociological_classification = 'Inferior sumergido'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_sociologicalclassification_CHOICES(self):
        self.valid.sociological_classification = 'Bad sociological classification'
        self.valid.save()
        self.assertRaises(ValidationError, self.valid.full_clean)


class TreeModelPhytosanitaryTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')

        self.field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=1
        )

        self.valid = Tree(field=self.field,
                          tree_id=1,
                          specie='Solanaceae',
                          dap=40,
                          dab=60,
                          tree_height=60,
                          latitude=-26,
                          longitude=-54,
                          picture=self.tempPicture,
                          obs='Teste 1',
                          phytosanitary_status='Bueno',
                          sociological_classification='Emergente')

    def test_phytosanitary_Bueno(self):
        self.valid.phytosanitary_status='Bueno'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Regular(self):
        self.valid.phytosanitary_status = 'Regular'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Malo(self):
        self.valid.phytosanitary_status = 'Malo'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_Muerto(self):
        self.valid.phytosanitary_status = 'Muerto'
        self.valid.save()
        self.assertTrue(Tree.objects.exists())

    def test_phytosanitary_CHOICES(self):
        """"Sociological classification mus be limited by choices"""
        self.valid.phytosanitary_status = 'BAD phytosanitary'
        self.valid.save()
        self.assertRaises(ValidationError, self.valid.full_clean)


class TreeModelGeomTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')

        self.field = TreeEcologicalData.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=1
        )

        self.tree = Tree.objects.create(
                field=self.field,
                tree_id=1,
                specie='Solanaceae',
                dap=40,
                dab=60,
                tree_height=60,
                latitude=-26,
                longitude=-54,
                picture=self.tempPicture,
                obs='Teste 1',
                phytosanitary_status='Bueno',
                sociological_classification='Emergente'
            )

    def test_exists(self):
        self.assertTrue(Tree.objects.exists())

    def test_geom_is_Point(self):
        self.assertEqual(self.tree.geom.get("type"), "Point")

    def test_geom_lon_Equals_lon_field(self):
        self.assertEqual(self.tree.geom.get("coordinates")[0], self.tree.longitude)

    def test_geom_lon_Equals_lat_field(self):
        self.assertEqual(self.tree.geom.get("coordinates")[1], self.tree.latitude)
