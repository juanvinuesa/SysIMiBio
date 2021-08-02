from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, Pictures, PermanentParcel, TreeMeasurement

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TreeMeasurementTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.staff = User.objects.create_user('Francisco', 'fran@imibio.com', 'fanpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=self.coordinator,
                                                      province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha', obs='Observacion', latitude=-26, longitude=-56,
                                                      geom='')
        self.field = FieldWork.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.parcel1
        )
        self.field.staff.add(self.staff)

        self.tree = Tree.objects.create(
            field=self.field,
            subplot='A1',
            tree_number=3,
            specie='Solanaceae',
            dap=40,
            dab=60,
            tree_height=60,
            latitude=-26,
            longitude=-54,
            picture=self.tempPicture,
            obs='Teste 1')

        self.valid_measurement = TreeMeasurement(
            field=self.field,
            tree=self.tree,
            dap=11,
            dab=20,
            tree_height=3,
            picture=self.tempPicture,
            phytosanitary_status='Bueno',
            sociological_classification='Emergente'
        )

    def test_tree_measurement_exists(self):
        self.valid_measurement.save()
        self.assertTrue(TreeMeasurement.objects.exists())

    def test_sociologicalclassification_Dominante(self):
        self.valid_measurement.sociological_classification = 'Dominante'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.sociological_classification, "Dominante")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Codominante(self):
        self.valid_measurement.sociological_classification = 'Codominante'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.sociological_classification, "Codominante")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Intermedia(self):
        self.valid_measurement.sociological_classification = 'Intermedia'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.sociological_classification, "Intermedia")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Inferior_suprimido(self):
        self.valid_measurement.sociological_classification = 'Inferior suprimido'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.sociological_classification, "Inferior suprimido")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Inferior_sumergido(self):
        self.valid_measurement.sociological_classification = 'Inferior sumergido'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.sociological_classification, "Inferior sumergido")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_CHOICES(self):
        self.valid_measurement.sociological_classification = 'Bad sociological classification'
        # self.valid_measurement.save()
        self.assertRaises(ValidationError, self.valid_measurement.full_clean) # todo debería ser full_clean()

    def test_phytosanitary_Regular(self):
        self.valid_measurement.phytosanitary_status = 'Regular'
        # self.valid_measurement.save()
        # self.assertEqual(self.valid_measurement.phytosanitary_status, "Regular")
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_Malo(self):
        self.valid_measurement.phytosanitary_status = 'Malo'
        # self.valid.save()
        # self.assertTrue(Tree.objects.exists())
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_Muerto(self):
        self.valid_measurement.phytosanitary_status = 'Muerto'
        # self.valid.save()
        # self.assertTrue(Tree.objects.exists())
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_CHOICES(self):
        """"Sociological classification mus be limited by choices"""
        self.valid_measurement.phytosanitary_status = 'BAD phytosanitary'
        # self.valid.save()
        self.assertRaises(ValidationError, self.valid_measurement.full_clean)  # todo debería ser full_clean()

# todo testar fotografia
    def test_str(self):
        """measurement string must be tree_id + field work date"""
        self.assertEqual('NTA13; 2020-12-30', str(self.valid_measurement))
