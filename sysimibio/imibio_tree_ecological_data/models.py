from django.db import models
# TODO insternaiconalizar los campos


class TreeEcologicalData(models.Model):

    EMERGENTE = 'Emergente'
    DOMINANTE = 'Dominante'
    CODOMINANTE = 'Codominante'
    INTERMEDIA = 'Intermedia'
    INFERIOR_SUPRIMIDO = 'Inferior suprimido'
    INFERIOR_SUMERGIDO = 'Inferior sumergido'
    SOCIOLOGICAL_CLASSIFICATION_CHOICES = [
        (EMERGENTE, 'Emergente'),
        (DOMINANTE, 'Dominante'),
        (CODOMINANTE, 'Codominante'),
        (INTERMEDIA, 'Intermedia'),
        (INFERIOR_SUPRIMIDO, 'Inferior Suprimido'),
        (INFERIOR_SUMERGIDO, 'Supeior Sumergido'),
    ]

    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    responsable = models.CharField(max_length=100)
    acompanantes = models.CharField(max_length=100)
    id_parcela = models.IntegerField()
    id_arbol = models.IntegerField()
    especie = models.CharField(max_length=100)
    dap = models.FloatField()
    dab = models.FloatField()
    altura = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    fotografia = models.URLField(null=True, blank=True)
    obs = models.TextField()
    estado_arbol = models.CharField(max_length=100)
    forma_vida = models.CharField(max_length=100)
    clasificacion_sociologica = models.CharField(
        max_length=100,
        choices=SOCIOLOGICAL_CLASSIFICATION_CHOICES,
        #default=FRESHMAN,
    )
    created_at = models.DateTimeField(auto_now_add=True)
