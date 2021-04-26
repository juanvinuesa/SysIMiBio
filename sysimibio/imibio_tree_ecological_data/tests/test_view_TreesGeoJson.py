from unittest import skip

from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree
from sysimibio.imibio_tree_ecological_data.forms import TreeForm


class TreesGeoJsonView(TestCase):
    def setUp(self):
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

        self.tree = TreeForm({
            'field':self.field,
            'tree_id':1,
            'specie':'Solanaceae',
            'dap':40.0,
            'dab':60.0,
            'tree_height':60.0,
            'latitude':-26.0,
            'longitude':-54.0,
            'obs':'Teste 1',
            'phytosanitary_status':'Bueno',
            'sociological_classification':'Emergente'
        })
        self.tree.save()
        self.occurrence = Tree.objects.all()[0]
        self.resp = self.client.get(r('data'))

    def test_get(self):
        """GET /geojson/ must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_keys(self):
        self.assertListEqual(['type', 'features', 'crs'], list(self.resp.json().keys()))

    def test_type(self):
        self.assertEqual("FeatureCollection", self.resp.json().get('type'))

    def test_crs(self):
        self.assertEqual("EPSG:4326", self.resp.json().get('crs').get("properties").get("name"))

    def test_properties(self):
        popup = self.resp.json().get('features')[0].get('properties').get('popup_content')
        self.assertEqual(popup, self.occurrence.popup_content)
