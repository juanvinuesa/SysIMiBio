# from django.contrib.auth.models import User
# from django.test import TestCase
# from geojson import Polygon
#
# from sysimibio.imibio_tree_ecological_data.models import PermanentParcel, Tree
# from sysimibio.imibio_tree_ecological_data.forms import TreeMeasurementForm
#
# # todo test validators. ver test_form_fieldRegistration
# class PermanenParcelFormTest(TestCase):
#     def setUp(self):
#         self.pemanent_plot1 = PermanentParcel.objects.create(
#             name="Reserva Yriapu",
#             coordinator=self.coordinator1,
#             province='Misiones',
#             municipality='Puerto Iguazú',
#             locality='600Ha',
#             obs='Parcela de prueba',
#             latitude=-26,
#             longitude=-54,
#             geom=Polygon([[(-54.6, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-54.6, -27.0)]]))
#
#         self.tree = Tree.objects.create(
#             field=self.pemanent_plot1,
#             subplot='A1',
#             tree_number=1,
#             specie='Solanaceae',
#             # dap=40,
#             # dab=60,
#             # tree_height=60,
#             latitude=-26,
#             longitude=-54,
#             # picture=self.tempPicture,
#             obs='Teste 1',
#             # phytosanitary_status='Bueno',
#             # sociological_classification='Emergente'
#         )
#         self.tree_measurement_form = TreeMeasurementForm()
#         self.coordinator1 = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
#
#
#     def create_PermanentParcelForm(self, **kwargs):
#         valid_form = dict(
#             name="YryaPu",
#             coordinator=self.coordinator1,
#             province='Misiones', municipality='Capital',
#             locality='600Ha', obs='Parcela de prueba', latitude=-26,
#             longitude=-54,
#             geom=Polygon([[(-54.6, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-54.6, -27.0)]]))
#         valid_form.update(**kwargs)
#         form = PermanentParcelForm(valid_form)
#         return form
#
#     def test_permanent_parcel_has_fields(self):
#         """Permanent Parcel form must have models fields"""
#         self.assertSequenceEqual(
#             ['name', 'coordinator', 'province', 'municipality', 'locality', 'obs', 'latitude', 'longitude',
#              'geom'], list(self.pp.fields))
#
#     def test_form_is_valid(self):
#         form = self.create_PermanentParcelForm()
#         self.assertTrue(form.is_valid())
#
#     def test_province_restriction(self):
#         """"province different from Misiones must return error"""
#         form = self.create_PermanentParcelForm(province="OtraProvincia")
#         self.assertFalse(form.is_valid())
#
#     def test_geom_is_invalid(self):
#         """"geom must be polygon geojson"""
#         form = self.create_PermanentParcelForm(geom=Point((-54.6, -27.0)))
#         self.assertFalse(form.is_valid())
#         self.assertEquals(form.errors["geom"][0], "Point does not match geometry type")
