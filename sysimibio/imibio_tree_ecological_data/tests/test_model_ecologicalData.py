from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, PermanentParcel


class TreeEcologicalRegistrationTest(TestCase):
    def setUp(self):
        coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        staff1 = User.objects.create_user('Feli', 'feli@imibio.com', 'felipassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test', province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha', obs='Observacion', latitude=-26, longitude=-56,
                                                      geom='')
        self.field = TreeEcologicalData(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=coordinator,
            parcel_id=self.parcel1)

        self.field.save()
        self.field.staff.add(staff1)

    def test_create(self):
        self.assertTrue(TreeEcologicalData.objects.exists())

    def test_created_at(self):
        """ecological registration must have an auto created_at attr."""
        self.assertIsInstance(self.field.created_at, datetime)

    def test_str(self):
        """str must be species name"""
        self.assertEqual('2020-12-30 Florencia', str(self.field))

    def test_modified_at(self):
        """registration must have and created at attr"""
        self.assertIsInstance(self.field.last_modification_at, datetime)
