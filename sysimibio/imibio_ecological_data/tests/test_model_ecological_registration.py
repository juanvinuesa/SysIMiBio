from django.test import TestCase

class TreeEcologicalRegistrationTest(TestCase):
    def setUp(self):
        self.obj = TreeEcologicalData(
            fecha='01/01/01',
            hora_inicio='0:0',
            hora_final='0:30',
            temperatura=35.9,
            humedad=80,
            responsable="Florencia",
            acompanantes="Felipe",
            id_parcela=1,
            id_arbol=1,
            especie='Solanaceae',
            dap=40,
            dab=60,
            altura=60,
            latitud=-43,
            longitud=-56,
            fotografia=True,
            obs='Teste 1',
            estado_arbol='Teste estado del arbol',
            forma_vida='Estado de vida',
            clasificacion_sociologica='Clasificacion de vida')
        self.resp = self.client.post('/registro_ecologico_arboreas/', self.data)
        self.obj.save()

    def test_create(self):
        self.assertTrue(TreeEcologicalData.objects.exists())
