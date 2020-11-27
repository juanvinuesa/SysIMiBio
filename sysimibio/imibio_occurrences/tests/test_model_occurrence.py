from datetime import datetime

from django.test import TestCase
from sysimibio.imibio_occurrences.models import ImibioOccurrence

class OcurrenceModelTest(TestCase):
    def setUp(self):
        self.obj = ImibioOccurrence(
            basisOfRecord='Observation',
            institutionCode=1,
            collectionCode=1,
            catalogNumber=2,
            scientificName='Pathera Onca',
            kingdom='reino',
            phylum='filo',
            clase='clase',
            order='orden',
            family='familia',
            genus='genero',
            specificEpithet='epiteto especifico',
            taxonRank='ranking de la taxonomia',
            infraspecificEpithet='infra espiteto',
            identificationQualifier='calificacion de identificacion',
            county='Argentina',
            stateProvince='Misiones',
            locality='Posadas',
            recordedBy='Felipe',
            recordNumber=1,
            decimalLatitude=-56,
            decimalLongitude=-60
        )
        self.obj.save()

    def test_creat(self):
        self.assertTrue(ImibioOccurrence.objects.exists())

    def test_created_at(self):
        """Registration must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
