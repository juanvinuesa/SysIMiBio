from django.db import models


class TreeEcologicalData(models.Model):

    # EMERGENTE = 'Emergente'
    # DOMINANTE = 'Dominante'
    # CODOMINANTE = 'Codominante'
    # INTERMEDIA = 'Intermedia'
    # INFERIOR_SUPRIMIDO = 'Inferior suprimido'
    # INFERIOR_SUMERGIDO = 'Inferior sumergido'
    # SOCIOLOGICAL_CLASSIFICATION_CHOICES = [
    #     (EMERGENTE, 'Emergente'),
    #     (DOMINANTE, 'Dominante'),
    #     (CODOMINANTE, 'Codominante'),
    #     (INTERMEDIA, 'Intermedia'),
    #     (INFERIOR_SUPRIMIDO, 'Inferior Suprimido'),
    #     (INFERIOR_SUMERGIDO, 'Supeior Sumergido'),
    # ]

    date = models.DateField(verbose_name='fecha')
    start_time = models.TimeField(verbose_name='hora_inicio')
    end_time = models.TimeField(verbose_name='hora_final')
    temperature = models.FloatField(verbose_name='temperatura')
    humidity = models.FloatField(verbose_name='humedad')
    coordinator = models.CharField(verbose_name='responsable', max_length=100)
    staff = models.CharField('acompanantes', max_length=100)
    parcel_id = models.IntegerField(verbose_name='ID parcela')
    tree_id = models.IntegerField(verbose_name='ID Árbol')
    specie = models.CharField(verbose_name='especie', max_length=100)
    dap = models.FloatField()
    dab = models.FloatField()
    tree_height = models.FloatField(verbose_name='Altura del árbol')
    latitude = models.FloatField(verbose_name='latitud')
    longitude = models.FloatField(verbose_name='longitud')
    photo = models.URLField(verbose_name='fotografia', null=True, blank=True)
    obs = models.TextField()
    tree_status = models.CharField(verbose_name='Estado del árbol', max_length=100)
    life_form = models.CharField(verbose_name='Forma de Vida', max_length=100)
    sociological_classification = models.CharField(verbose_name='clasificación sociologica',
        max_length=100
        # choices=SOCIOLOGICAL_CLASSIFICATION_CHOICES,
        #default=FRESHMAN,
    )
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    last_modification_at = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)

    class Meta:
        verbose_name_plural = 'Registro de campo'
        verbose_name =  'Campo'
        ordering = ('-date', )

    def __str__(self):
        return f'{self.date} {self.coordinator}'


class Tree(models.Model):
    field = models.ForeignKey('TreeEcologicalData', on_delete=models.CASCADE) # ao deletar um registro de campo os dados de arvore tbm o serao
    tree_id = models.IntegerField(verbose_name='ID Árbol')
    specie = models.CharField(verbose_name='especie', max_length=100)
    dap = models.FloatField()
    dab = models.FloatField()
    tree_height = models.FloatField(verbose_name='Altura del árbol')
    latitude = models.FloatField(verbose_name='latitud')
    longitude = models.FloatField(verbose_name='longitud')
    photo = models.URLField(verbose_name='fotografia', null=True, blank=True)
    obs = models.TextField()
    tree_status = models.CharField(verbose_name='Estado del árbol', max_length=100)
    life_form = models.CharField(verbose_name='Forma de Vida', max_length=100)
    sociological_classification = models.CharField(verbose_name='clasificación sociologica',
                                                   max_length=100)

