from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from djgeojson.fields import PointField, PolygonField
from geojson import Point
from sysimibio.toolbox import create_subplot_name_choices
from sysimibio.imibio_tree_ecological_data.validators import validate_date, validate_temperature, validate_humidity, \
    validate_lat, validate_lon, tree_height_validation, tree_dap_validation


class PermanentParcel(models.Model):
    name = models.CharField(verbose_name="Nombre de la parcela", max_length=50)
    coordinator = models.ForeignKey(User, verbose_name='Responsable', max_length=100, on_delete=models.CASCADE, blank=True, default='')
    province = models.CharField(verbose_name="Provincia", choices=(('Misiones', 'Misiones'),), max_length=10)
    municipality = models.CharField(verbose_name="Municipio", max_length=50) # TODO add 75 municipio como choices
    locality = models.CharField(verbose_name="Localidad", max_length=50)
    obs = models.TextField(verbose_name="Obervaciones", blank=True)
    latitude = models.FloatField(verbose_name='Latitud',
                                 validators=[validate_lat], blank=True, help_text="informar en formato en grados decimales WGS84 - epsg4326")
    longitude = models.FloatField(verbose_name='Longitud', validators=[validate_lon], blank=True, help_text="informar en formato en grados decimales WGS84 - epsg4326")
    geom = PolygonField(blank=True)

    @property
    def geom_point(self):
        return Point((self.longitude, self.latitude))

    @property
    def parcel_initials(self):
        return ''.join([x[0].upper() for x in self.name.split(' ')])

    def __str__(self):
        return f'{self.name}, {self.municipality} - {self.locality}'

    class Meta:
        verbose_name_plural = 'Parcelas Permanentes'
        verbose_name = 'Parcela Permanente'


class FieldWork(models.Model):
    date = models.DateField(verbose_name='Fecha', validators=[validate_date], help_text='ej.: AAAA-MM-DD')
    start_time = models.TimeField(verbose_name='Hora inicio', help_text='ej.: 12:30')
    end_time = models.TimeField(verbose_name='Hora final', help_text='ej.: 13:00')
    temperature = models.FloatField(verbose_name='Temperatura', validators=[validate_temperature], help_text='°C')
    humidity = models.FloatField(verbose_name='Humedad', validators=[validate_humidity], help_text='%')
    coordinator = models.ForeignKey(User, verbose_name='Responsable', max_length=100, on_delete=models.CASCADE)
    staff = models.ManyToManyField(User, related_name='staff', verbose_name='Acompanantes',
                                   max_length=100)
    parcel_id = models.ForeignKey("PermanentParcel", verbose_name='Parcela Permanente', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    last_modification_at = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)

    class Meta:
        verbose_name_plural = 'Registros de campo'
        verbose_name = 'Campo'
        ordering = ('-date', )

    def __str__(self):
        return f'{self.date} {self.coordinator}'


class Pictures(models.Model):
    picture = models.ImageField(verbose_name="Fotografía", null=True, blank=True, help_text='Choose foto')

    class Meta:
        verbose_name = 'Fotografía'
        verbose_name_plural = 'Fotografías'


class Tree(models.Model):
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

    BUENO = 'Bueno'
    REGULAR = 'Regular'
    MALO = 'Malo'
    MUERTO = 'Muerto'
    PHYTOSANITARY_STATUS_CHOICES = [
        (BUENO, 'Bueno'),
        (REGULAR, 'Regular'),
        (MALO, 'Malo'),
        (MUERTO, 'Muerto')
    ]

    SUBPLOTS_CHOICES = create_subplot_name_choices(2,2)

    field = models.ForeignKey('FieldWork', on_delete=models.CASCADE)
    subplot = models.CharField(verbose_name="Sub parcela", choices=SUBPLOTS_CHOICES, max_length=4)
    specie = models.CharField(verbose_name='Nombre especie', max_length=100)
    dap = models.FloatField(verbose_name='DAP', help_text='cm', validators=[tree_dap_validation], default=SUBPLOTS_CHOICES[0][0])
    dab = models.FloatField(verbose_name='DAB', help_text='cm') # hace parte de la medición?
    tree_height = models.FloatField(verbose_name='Altura del árbol', help_text='m', validators = [tree_height_validation]) # hace parte de la medición?
    latitude = models.FloatField(verbose_name='Latitud', validators=[validate_lat], help_text="informar en formato graus decimais WGS84")
    longitude = models.FloatField(verbose_name='Longitud', validators=[validate_lon])
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE, blank=True, null = True)
    obs = models.TextField(verbose_name="Observaciones", blank=True)
    phytosanitary_status = models.CharField(max_length=100, # hace parte de la medición?
                                            choices=PHYTOSANITARY_STATUS_CHOICES,
                                            default=BUENO)
    sociological_classification = models.CharField(verbose_name='Clasificación sociologica', # hace parte de la medición?
                                                   max_length=100,
                                                   choices=SOCIOLOGICAL_CLASSIFICATION_CHOICES,
                                                   default=EMERGENTE)
    geom = PointField(blank=True)

    @property
    def tree_id(self):
        return ''.join(x[0].upper() for x in self.field.parcel_id.name.split(' ')) # todo add subparcela

    class Meta:
        verbose_name = 'Árbol'
        verbose_name_plural = 'Árboles'

    def __str__(self):
        return f'{self.specie} {self.field.date}'

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:detail', kwargs={'pk': self.pk})

    @property
    def popup_content(self): # todo Me parece que lo importante es poner alguna foto
        popup = "<strong><span>Nombre científico: </span>{}</strong></p>".format(
            self.specie)
        popup += "<span>DAP: </span>{}<br>".format(
            self.dap)
        popup += "<span>Altura: </span>{}<br>".format(
            self.tree_height)
        popup += f"<span><a href={self.get_absolute_url()}>Detalles de la occurrencia</a></strong><br>"
        return popup
