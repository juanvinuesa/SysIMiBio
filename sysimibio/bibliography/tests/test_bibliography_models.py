from django.contrib.auth.models import User
from django.test import TestCase
from sysimibio.bibliography.models import Publication
from datetime import datetime


class PublicationModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="myusername", password="password", email="abc@testmail.com")
        self.p1 = Publication.objects.create(
            crossref=False,
            title='Jorge el curioso',
            publication_year='2001',
            author='juan',
            created_by=user,
            URL='http://bibliotecadigital.ilce.edu.mx/Colecciones/ObrasClasicas/_docs/TeoriaEvolucion-Darwin.pdf',
            ORCID='https://orcid.org/0000-0002-1825-0097',
        )
        self.p2 = Publication.objects.create(
            DOI='10.1038/s41467-021-22702-2',
            created_by=user)
        self.p3 = Publication.objects.create(
            ISBN='9780300206111',
            created_by=user
        )

    #         self.obj1 = Publication.create(
    #             id=56,
    #             DOI='10.1038/s41467-021-22702-2',
    #             publication_year='1940',
    #             title='lectura obligatoria',
    #             created_by=user,
    #             author='juan',
    #             ISBN='9780300206111',
    #             subject='Life',
    #             # ORCID='dadasd',
    #             # URL='https://www.google.com/',
    #             # created_at=datetime.datetime[11,32,1940],
    #             # last_modification_at=datetime.datetime[13,31,1232],
    #             # observations='3ddasdsa',
    #             # imibio=False,
    #             # crossref=True,
    #
    #         )
    #
    # // todo Fijarse si hay que testear todos los campos
    def test_check_object(self):
        self.assertTrue(Publication.objects.exists())

    def test_count_created_objects(self): #must be 3 //
        self.assertEqual(Publication.objects.count(), 3)

    def test_object_content(self):
        p1 = Publication.objects.get(title='Jorge el curioso')
        self.assertEqual(p1.title, 'Jorge el curioso')
        self.assertEqual(p1.author, 'juan')
        self.assertEqual(p1.publication_year, '2001')
        self.assertEqual(p1.observations, '')
        self.assertEqual(p1.subject, '')
        self.assertEqual(p1.ORCID, 'https://orcid.org/0000-0002-1825-0097')
        self.assertEqual(p1.URL, 'http://bibliotecadigital.ilce.edu.mx/Colecciones/ObrasClasicas/_docs/TeoriaEvolucion-Darwin.pdf')

    def test_check_object_is_article(self):
        self.assertTrue(self.p2.DOI)

    def test_check_object_is_book(self):
        self.assertTrue(self.p3.ISBN)

    def test_check_object_is_not_registered_publication(self):
        self.assertFalse(self.p1.DOI)
        self.assertFalse(self.p1.ISBN)
        self.assertTrue(self.p1.title)
        self.assertTrue(self.p1.publication_year)
        self.assertTrue(self.p1.author)
        self.assertFalse(self.p1.crossref)

    def test_str(self):
        """Publication str must be author, publication_year - title"""
        self.assertEqual('juan, 2001 - Jorge el curioso', str(self.p1))

    def test_created_at(self):
        """Publication  must have an auto created_at attr."""
        self.assertIsInstance(self.p1.created_at, datetime)

    def test_last_modification(self):
        self.assertIsInstance(self.p1.last_modification_at, datetime)

    def test_created_by(self):
        self.assertIsInstance(self.p1.created_by, User)

    def test_crossref_boolean(self):
        self.assertTrue(self.p2.crossref)

    def test_imibio_default_boolean(self):
        self.assertFalse(self.p2.imibio)

    def test_Url_field(self):
        self.assertEqual(self.p1.URL, "http://bibliotecadigital.ilce.edu.mx/Colecciones/ObrasClasicas/_docs/TeoriaEvolucion-Darwin.pdf")

    def test_ORCID_field(self):
        self.assertEqual(self.p1.ORCID, 'https://orcid.org/0000-0002-1825-0097')