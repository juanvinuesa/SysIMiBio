from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, Pictures, PermanentParcel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


# todo pregunta fotos asociada al arbol, a la medición o al campo?
@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TreeModelSociologicalTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=coordinator,
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
            coordinator=coordinator,
            parcel_id=self.parcel1
        )

        self.valid = Tree(field=self.field,
                          specie='Solanaceae',
                          latitude=-26,
                          longitude=-54,
                          picture=self.tempPicture,
                          obs='Teste 1')


class TreeModelPropertiesTest(TestCase):
    def setUp(self):
        self.tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=coordinator,
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
            coordinator=coordinator,
            parcel_id=self.parcel1
        )

        self.tree = Tree.objects.create(
            field=self.field,
            subplot='A1',
            tree_number=1,
            specie='Solanaceae',
            latitude=-26,
            longitude=-54,
            picture=self.tempPicture,
            obs='Teste 1')

    def test_popup(self):
        self.assertEqual(self.tree.popup_content,
                         "<strong><span>Nombre científico: </span>Solanaceae</strong></p><span><a href=/imibio_tree_ecological_data/1/>Detalles de la occurrencia</a></strong><br>")

    def test_tree_id(self):
        self.assertEqual(self.tree.tree_id,
                         "NTA11")
