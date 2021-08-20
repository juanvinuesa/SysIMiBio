from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from geojson import Polygon, Point

from sysimibio.imibio_tree_ecological_data.forms import FieldForm
from sysimibio.imibio_tree_ecological_data.models import FieldWork, PermanentParcel


class FieldWorkListView(TestCase):
    def setUp(self):
        self.coordinator = User.objects.create_user('Florencia',
                                                    'flor@imibio.com',
                                                    'florpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=self.coordinator,
                                                      province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha',
                                                      obs='Observacion',
                                                      latitude=-26,
                                                      longitude=-56,
                                                      geom='')
        self.field1 = FieldWork.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.parcel1
        )
        self.field1.save()
        self.field1.staff.add(self.coordinator)

        self.field2 = FieldWork.objects.create(
            date='2020-11-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.parcel1
        )

        self.resp = self.client.get(r('imibio_tree_ecological_data:field_list'))

    def test_get(self):
        """GET /field_list/ must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_use_template(self):
        """GET /field_list/ must use fieldwork_list.html template"""
        self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/fieldwork_list.html')

    def test_list(self):
        """GET /field_list/ must have the same queryset from database"""
        all_entries = FieldWork.objects.all()
        self.assertQuerysetEqual(self.resp.context['fieldwork_list'],
                         all_entries, ordered=False)


class PermanentParcelDetailView(TestCase):
    def setUp(self):
        self.coordinator = User.objects.create_user('Florencia',
                                                    'flor@imibio.com',
                                                    'florpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Reserva Yrya Pu',
                                                      coordinator=self.coordinator,
                                                      province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha',
                                                      obs='Observacion',
                                                      latitude=-26,
                                                      longitude=-56,
                                                      geom='')
        self.field1 = FieldWork.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.parcel1
        )

        self.resp = self.client.get(r('imibio_tree_ecological_data:field_detail', 1))

    def test_get(self):
        """GET /field_detail/1 must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_detail_use_template(self):
        """GET /field_detail/1 must use fieldwork_detail.html template"""
        self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/fieldwork_detail.html')

    def test_detail_html(self): # todo testar mapa
        content = [
            'Reserva Yrya Pu, Puerto Iguazu - 600 ha',
            'Florencia',
            '30 de Diciembre de 2020',
            '0:0',
            '0:30',
            '35,9',
            '80,0'
        ]
        with self.subTest():
            for expected in content:
                self.assertContains(self.resp, expected)


class PermanentParcelDetailNotFound(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('imibio_tree_ecological_data:field_detail', 0))

    def test_not_found(self):
        self.assertEqual(404, self.resp.status_code)


# class PermanentParcelCreate(TestCase):
#     def setUp(self):
#         self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
#         self.pp_form = PermanentParcelForm
#         self.resp = self.client.get(r('imibio_tree_ecological_data:plot_create'))
#         # todo testar post
#
#     def test_get(self):
#         """GET /plot_create must get status code 200"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_template(self):
#         """must use imibio_tree_ecological_data/permanentparcel_form.html"""
#         self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/permanentparcel_form.html')
#
#     def test_html(self):
#         """HTML must contais input tags"""
#         tags = ( # todo confirmar las tags a seren testadas
#             ('<form'),
#             ('<input'),
#             ('type="text"'),
#             ('type="submit"')
#             )
#         # for text in tags:
#         #     with self.subTest():
#         #         self.assertContains(self.resp, text)
#
#     def test_csrf(self):
#         """html must contains CSRF"""
#         self.assertContains(self.resp, 'csrfmiddlewaretoken')
#
#     def test_has_form(self):
#         """"Context must have permanentparcel create form"""
#         form = self.resp.context['form']
#         self.assertIsInstance(form, PermanentParcelForm)
#

# class PermanentParcelEdit(TestCase):
#     def setUp(self):
#         self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
#         self.pp1 = PermanentParcel.objects.create(
#             name="Reserva Yrya Pu",
#             coordinator=self.coordinator,
#             province="Misiones",
#             municipality="Puerto Iguazú",
#             locality='reserva 600 ha',
#             obs="Prueba de registro",
#             latitude=-26,
#             longitude=-54,
#             geom=Polygon([[(-54.6, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-54.6, -27.0)]])
#         )
#         self.resp = self.client.get(r('imibio_tree_ecological_data:plot_edit', self.pp1.pk))
#
#     def test_get(self):
#         """GET /plot_create must get status code 200"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_template(self):
#         """must use imibio_tree_ecological_data/permanentparcel_form.html"""
#         self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/permanentparcel_form.html')
#
#     def test_html(self):
#         """HTML must contais input tags"""
#         tags = (  # todo confirmar las tags a seren testadas
#             ('<form'),
#             ('<input'),
#             ('type="text"'),
#             ('type="submit"')
#         )
#         # for text in tags:
#         #     with self.subTest():
#         #         self.assertContains(self.resp, text)
#
#     def test_csrf(self):
#         """html must contains CSRF"""
#         self.assertContains(self.resp, 'csrfmiddlewaretoken')
#
#     def test_has_form(self):
#         """"Context must have permanentparcel create form"""
#         form = self.resp.context['form']
#         self.assertIsInstance(form, PermanentParcelForm)
#
#     def test_update(self):
#         update = {'name': 'Campo San Juan',
#                   'coordinator': self.coordinator,
#                   'province': 'Misiones',
#                   'municipality': 'Campo San Juan',
#                   'locality': 'Campo San Juan',
#                   'obs': 'observacion update',
#                   'latitude': -26,
#                   'longitude': -56,
#                   'geom': self.pp1.geom,
#                   'geom_point': self.pp1.geom_point}
#
#         # response = self.client.post(
#         #     r('imibio_tree_ecological_data:plot_edit', self.pp1.pk),
#         #     update)
#
#         # self.assertEqual(response.status_code, 302) # todo arreglar
#
#         # self.pp1.refresh_from_db()
#         # self.assertEqual(self.pp1.name, "Campo San Juan") # todo no anda. Fran tendrá que arreglar :)
