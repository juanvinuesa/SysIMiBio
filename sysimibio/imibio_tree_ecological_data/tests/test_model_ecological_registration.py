from datetime import datetime

from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeEcologicalRegistrationTest(TestCase):
    def setUp(self):
        self.obj = TreeEcologicalData(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator="Florencia",
            staff='Felipe',
            parcel_id=1)
        self.obj.save()

    def test_create(self):
        self.assertTrue(TreeEcologicalData.objects.exists())

    def test_created_at(self):
        """ecological registration must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """str must be species name"""
        self.assertEqual('2020-12-30 Florencia', str(self.obj))

    def test_modified_at(self):
        """registration must have and created at attr"""
        self.assertIsInstance(self.obj.last_modification_at, datetime)
