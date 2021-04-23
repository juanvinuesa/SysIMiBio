from django.test import TestCase
from django.core.exceptions import ValidationError
from sysimibio.imibio_tree_ecological_data.models import PermanentParcel
# from django.contrib.auth.models import User


class PermanentParcelModelTest(TestCase):
    def setUp(self):
        self.pp1 = PermanentParcel.objects.create(
            nombre = "Reserva Yrya Pu",
            province = "Misiones",
            municipality = "Puerto Iguazú",
            locality = 'reserva 600 ha',
            obs = "Prueba de registro",
            latitude=-26,
            longitude=-54
        )
    def test_permanentparcel_model(self):
        self.assertTrue(PermanentParcel.objects.exists())

    def test_print(self):
        self.assertEqual(str(self.pp1), "Reserva Yrya Pu, Puerto Iguazú - reserva 600 ha")
