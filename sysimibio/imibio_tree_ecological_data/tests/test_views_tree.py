from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from geojson import Polygon, Point

from sysimibio.imibio_tree_ecological_data.forms import TreeForm
from sysimibio.imibio_tree_ecological_data.models import Tree, PermanentParcel, FieldWork


class TreeCreateView(TestCase):
    def setUp(self):
        self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.staff1 = User.objects.create_user('Feli', 'feli@imibio.com', 'felipassword')
        self.staff2 = User.objects.create_user('Fran', 'Fran@imibio.com', 'Franpassword')
        self.permanent_parcel = PermanentParcel.objects.create(
                name="Reserva Yrya Pu",
                coordinator=self.coordinator,
                province="Misiones",
                municipality="Puerto Iguazú",
                locality="reserva 600 ha",
                obs="Prueba de registro",
                latitude=-26,
                longitude=-56,
                geom='{"coordinates": [[[-54.6, -27.0], [-54.0, -27.07], [-54.07, -26.62], [-54.6, -27.0]]], "type": "Polygon"}')
        self.field = FieldWork(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.permanent_parcel)

        self.field.save()
        self.field.staff.add(self.staff1)
        self.field.staff.add(self.staff2)

        self.resp = self.client.get(r('imibio_tree_ecological_data:tree_create'))

    def test_get(self):
        """GET /tree_create must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """must use imibio_tree_ecological_data/tree_form.html"""
        self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/tree_form.html')

    # def test_html(self):
    #     """HTML must contais input tags"""
    #     tags = (  # todo confirmar las tags a seren testadas
    #         ('<form'),
    #         ('<input'),
    #         ('type="text"'),
    #         ('type="submit"')
    #     )
    #     # for text in tags:
    #     #     with self.subTest():
    #     #         self.assertContains(self.resp, text)

    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have tree create form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, TreeForm)

    def test_valid_post(self):
        data = {
            'field': self.field.pk,
            'subplot': 'A1',
            'tree_number': 1,
            'specie': "spp1",
            'latitude': -26,
            'longitude': -54.5
        }
        post_response = self.client.post(r('imibio_tree_ecological_data:tree_create'), data)
        self.assertTrue(Tree.objects.exists())
        self.assertRedirects(post_response, r('imibio_tree_ecological_data:tree_detail', 1))

    def test_invalid_post(self):
        data = { # todo fazer teste passar
            'field': self.field.pk,
            'subplot': 'A1',
            'tree_number': 1,
            'specie': 'spp1',
            'latitude': -26,
            'longitude': -54.5
        }
        post_response = self.client.post(r('imibio_tree_ecological_data:tree_create'), data)
        self.assertFalse(Tree.objects.exists())
        # self.assertTrue(post_response.status_code, 200)


# class PermanentParcelEditView(TestCase):
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
#         """GET plot/create must get status code 200"""
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
#         update = {
#             'name': "Campo San Juan",
#             'coordinator': self.coordinator.pk,
#             'province': "Misiones",
#             'municipality': "Puerto Iguazú",
#             'locality': "reserva 600 ha",
#             'obs': "Prueba de registro",
#             'latitude': -26,
#             'longitude': -56,
#             'geom': '{"coordinates": [[[-54.6, -27.0], [-54.0, -27.07], [-54.07, -26.62], [-54.6, -27.0]]], "type": "Polygon"}'
#         }
#
#         post_response = self.client.post(r('imibio_tree_ecological_data:plot_edit', self.pp1.pk), update)
#
#         self.assertRedirects(post_response, r('imibio_tree_ecological_data:plot_detail', self.pp1.pk))
#
#         self.pp1.refresh_from_db()
#         self.assertEqual(self.pp1.name, "Campo San Juan")
#
#
# class PermanentParcelListView(TestCase):
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
#         self.pp2 = PermanentParcel.objects.create(
#             name="Campoo San Juan",
#             coordinator=self.coordinator,
#             province="Misiones",
#             municipality="Posadas",
#             locality='Campo San Juan',
#             obs="Prueba de registro 2",
#             latitude=-26.002,
#             longitude=-56,
#             geom=Polygon([[(-56, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-56, -27.0)]])
#         )
#
#         self.resp = self.client.get(r('imibio_tree_ecological_data:plot_list'))
#
#     def test_get(self):
#         """GET /plot_list/ must get status code 200"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_use_template(self):
#         """GET /plot_list/ must use permanentparcel_list.html template"""
#         self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/permanentparcel_list.html')
#
#     def test_list(self):
#         """GET /plot_list/ must have the same queryset from database"""
#         all_entries = PermanentParcel.objects.all()
#         self.assertQuerysetEqual(self.resp.context['permanentparcel_list'],
#                                  all_entries, ordered=False)
#
#
# class PermanentParcelDetailView(TestCase):
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
#         self.resp = self.client.get(r('imibio_tree_ecological_data:plot_detail', 1))
#
#     def test_get(self):
#         """GET /plot_detail/1 must get status code 200"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_detail_use_template(self):
#         """GET /plot_detail/1 must use permanentparcel_detail.html template"""
#         self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/permanentparcel_detail.html')
#
#     def test_detail_html(self):  # todo testar mapa
#         content = [
#             "Reserva Yrya Pu",
#             "Reserva Yrya Pu",
#             "Florencia",
#             "Misiones",
#             "Puerto Iguazú",
#             'reserva 600 ha',
#             "Prueba de registro"]
#         with self.subTest():
#             for expected in content:
#                 self.assertContains(self.resp, expected)
#
#
# class PermanentParcelDetailNotFound(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('imibio_tree_ecological_data:plot_detail', 0))
#
#     def test_not_found(self):
#         self.assertEqual(404, self.resp.status_code)
