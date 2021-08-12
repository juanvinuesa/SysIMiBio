from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from geojson import Polygon

from sysimibio.imibio_tree_ecological_data.models import PermanentParcel


class PermanentParcelListView(TestCase):
    def setUp(self):
        self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.pp1 = PermanentParcel.objects.create(
            name="Reserva Yrya Pu",
            coordinator=self.coordinator,
            province="Misiones",
            municipality="Puerto Iguazú",
            locality='reserva 600 ha',
            obs="Prueba de registro",
            latitude=-26,
            longitude=-54,
            geom=Polygon([[(-54.6, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-54.6, -27.0)]])
        )
        self.pp2 = PermanentParcel.objects.create(
            name="Campoo San Juan",
            coordinator=self.coordinator,
            province="Misiones",
            municipality="Posadas",
            locality='Campo San Juan',
            obs="Prueba de registro 2",
            latitude=-26.002,
            longitude=-56,
            geom=Polygon([[(-56, -27.0), (-54.0, -27.07), (-54.07, -26.62), (-56, -27.0)]])
        )

        self.resp = self.client.get(r('imibio_tree_ecological_data:plot_list'))

    def test_get(self):
        """GET /plot_list/ must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_use_template(self):
        """GET /plot_list/ must use permanentparcel_list.html template"""
        self.assertTemplateUsed(self.resp, 'imibio_tree_ecological_data/permanentparcel_list.html')

    def test_list(self):
        """GET /plot_list/ must have the same queryset from database"""
        all_entries = PermanentParcel.objects.all()
        self.assertQuerysetEqual(self.resp.context['permanentparcel_list'],
                         all_entries, ordered=False)
