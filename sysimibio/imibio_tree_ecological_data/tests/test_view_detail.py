from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.shortcuts import resolve_url as r
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree, Pictures

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TreeEcologicalRegistrationDetailGet(TestCase):
    def setUp(self):
        tempPicture = Pictures.objects.create(picture=SimpleUploadedFile('tiny.gif', TINY_GIF))
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        staff1 = User.objects.create_user('Juan', 'Juan@imibio.com', 'Juanpassword')


        self.obj = TreeEcologicalData.objects.create(
            date='2020-12-31',
            start_time='12:22',
            end_time='13:23',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=1
        )
        self.obj.staff.add(staff1)

        self.tree = Tree.objects.create(
            field=self.obj,
            tree_id=1,
            specie='Solanaceae',
            dap=40,
            dab=60,
            tree_height=60,
            latitude=-26,
            longitude=-54,
            picture = tempPicture,
            obs='Teste 1',
            phytosanitary_status='Bueno',
            sociological_classification='Emergente'
        )

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
            1,
            '31 de Diciembre de 2020',
            '12:22',
            '13:23',
            35,9,
            80,
            'Florencia',
            'Juan',
            1,
            1,
            'Solanaceae',
            40,
            60,
            60,
            -26,
            -54,
            'Teste 1',
            'Bueno',
            'Emergente'
            )
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

class TreeEcologicalRegistrationDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('imibio_tree_ecological_data:detail', 0))
        self.assertEqual(404, resp.status_code)
