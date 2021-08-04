from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import resolve_url as r
from django.test import TestCase, override_settings

from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, Pictures, PermanentParcel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TreeEcologicalRegistrationDetailGet(TestCase):
    def setUp(self):
        tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        staff1 = User.objects.create_user('Juan', 'Juan@imibio.com', 'Juanpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test', province='Misiones',
                                                      coordinator=coordinator,
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha', obs='Observacion', latitude=-26, longitude=-56,
                                                      geom='')

        self.obj = FieldWork.objects.create(
            date='2020-12-31',
            start_time='12:22',
            end_time='13:23',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=self.parcel1
        )
        self.obj.staff.add(staff1)

        self.tree = Tree.objects.create(
            field=self.obj,
            subplot='A1',
            tree_number=1,
            specie='Solanaceae',
            latitude=-26,
            longitude=-54,
            picture = tempPicture,
            obs='Teste 1')

        self.resp = self.client.get(r('imibio_tree_ecological_data:detail', self.tree.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'tree_ecological_detail.html')

    def test_context(self):
        tree_detail = self.resp.context['tree_detail']
        self.assertIsInstance(tree_detail, Tree)

    def test_html(self):
        content = (
            'Solanaceae',
            '31 de Diciembre de 2020',
            '12:22',
            '13:23',
            35,9,
            80,
            'Florencia',
            'Juan',
            1,
            'Solanaceae',
            -26,
            -54,
            'Teste 1',
            )
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

class TreeEcologicalRegistrationDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('imibio_tree_ecological_data:detail', 0))
        self.assertEqual(404, resp.status_code)
