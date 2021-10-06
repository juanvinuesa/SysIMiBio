from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from djgeojson.fields import PointField, PolygonField
from geojson import Point

from sysimibio.imibio_tree_ecological_data.validators import validate_date, validate_temperature, validate_humidity, \
    validate_lat, validate_lon, tree_height_validation, tree_dap_validation
from sysimibio.toolbox import create_subplot_name_choices


class PermanentParcel(models.Model):  # todo change to Permanent Plot?
    name = models.CharField(verbose_name='Nombre de la parcela', max_length=50)
    coordinator = models.ForeignKey(User, verbose_name='Responsable', max_length=100, on_delete=models.CASCADE)
    province = models.CharField(verbose_name='Provincia', choices=(('Misiones', 'Misiones'),), max_length=10)
    municipality = models.CharField(verbose_name='Municipio',
                                    max_length=50)  # TODO add 75 municipio como choices o como geojson FK
    locality = models.CharField(verbose_name='lugar', max_length=50)
    cadastral_parcel = models.BigIntegerField(verbose_name='Nomenclatura catastral', help_text='Verificar en <a href="http://ide.ordenamientoterritorial.misiones.gob.ar/index.php?option=com_content&view=article&id=8&Itemid=3"> GeoMisiones (IDE Misiones)</a>, capa "Parcelario Misiones', default=0000000000000000000)
    plot_type = models.CharField(verbose_name='Tipo de parcela', choices=(('Publico', 'Publico'), ('Privado', 'Privado')), max_length=10, default='Publico')
    obs = models.TextField(verbose_name='Obervaciones', blank=True)
    latitude = models.FloatField(verbose_name='Latitud',
                                 validators=[validate_lat], blank=True,
                                 help_text="informar en formato en grados decimales WGS84 - epsg4326")
    longitude = models.FloatField(verbose_name='Longitud', validators=[validate_lon], blank=True,
                                  help_text="informar en formato en grados decimales WGS84 - epsg4326")
    geom = PolygonField(blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True, null=True)

    @property
    def geom_point(self):
        return Point((self.longitude, self.latitude))

    @property
    def parcel_initials(self):
        return ''.join([x[0].upper() for x in self.name.split(' ')])

    def __str__(self):
        return f'{self.name}, {self.municipality} - {self.coordinator}'

    class Meta:
        verbose_name_plural = 'Parcelas Permanentes'
        verbose_name = 'Parcela Permanente'

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:plot_detail', kwargs={'pk': self.pk})

    @property
    def popup_content(self):
        popup = f"<strong><span>Parcela: </span>{self.name}</strong></p>"
        popup += f"<strong><span>Coordinador: </span>{self.coordinator}</strong></p>"
        popup += f"<span><a href={self.get_absolute_url()}>Detalles de la parcela</a></strong><br>"
        return popup


class FieldWork(models.Model):
    date = models.DateField(verbose_name='Fecha', validators=[validate_date], help_text='ej.: AAAA-MM-DD')
    start_time = models.TimeField(verbose_name='Hora inicio', help_text='ej.: 12:30')
    end_time = models.TimeField(verbose_name='Hora final', help_text='ej.: 13:00')
    temperature = models.FloatField(verbose_name='Temperatura', validators=[validate_temperature], help_text='°C')
    humidity = models.FloatField(verbose_name='Humedad', validators=[validate_humidity], help_text='%')
    coordinator = models.ForeignKey(User, verbose_name='Responsable', max_length=100, on_delete=models.CASCADE)
    staff = models.ManyToManyField(User, related_name='staff', verbose_name='Acompanantes',
                                   max_length=100)
    parcel_id = models.ForeignKey("PermanentParcel", verbose_name='Parcela Permanente',
                                  on_delete=models.CASCADE)  # todo mudar nombre?
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    last_modification_at = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)

    class Meta:
        verbose_name_plural = 'Registros de campo'
        verbose_name = 'Campo'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.parcel_id}-{self.date}'

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:field_detail', kwargs={'pk': self.pk})


class Pictures(models.Model):
    picture = models.ImageField(verbose_name="Fotografía", null=True, blank=True, help_text='Choose foto')

    class Meta:
        verbose_name = 'Fotografía'
        verbose_name_plural = 'Fotografías'


class Tree(models.Model):
    SUBPLOTS_CHOICES = create_subplot_name_choices(10, 10)

    field = models.ForeignKey('FieldWork', on_delete=models.CASCADE)
    # todo por que no tiene relación con parcela permannente?
    subplot = models.CharField(verbose_name="Sub parcela", choices=SUBPLOTS_CHOICES, max_length=5, default='A1')
    tree_number = models.PositiveIntegerField(verbose_name="Numero del árbol", default=1)
    specie = models.CharField(verbose_name='Nombre especie',
                              max_length=100)  # todo cambiar nombre del campo manteniendo consistente con otros models
    latitude = models.FloatField(verbose_name='Latitud', validators=[validate_lat],
                                 help_text="informar en grados decimales - WGS84")
    longitude = models.FloatField(verbose_name='Longitud', validators=[validate_lon],
                                  help_text="informar en grados decimales - WGS84")
    obs = models.TextField(verbose_name="Observaciones", blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True, null=True)
    geom = PointField(blank=True)

    @property
    def tree_id(self):
        return f"{''.join(x[0].upper() for x in self.field.parcel_id.name.split(' '))}{self.subplot}{self.tree_number}"

    class Meta:
        verbose_name = 'Árbol'
        verbose_name_plural = 'Árboles'

    def __str__(self):
        return f'{self.tree_id} {self.specie} {self.field.date}'

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:tree_detail', kwargs={'pk': self.pk})

    @property
    def popup_content(self):
        popup = "<strong><span>Nombre científico: </span>{}</strong></p>".format(
            self.specie)
        popup += f"<span><a href={self.get_absolute_url()}>Detalles del árbol</a></strong><br>"
        return popup


class TreeMeasurement(models.Model):
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

    field = models.ForeignKey("FieldWork", on_delete=models.CASCADE)
    tree = models.ForeignKey("Tree", on_delete=models.CASCADE)
    dap = models.FloatField(verbose_name='DAP', help_text='cm', validators=[tree_dap_validation])
    dab = models.FloatField(verbose_name='DAB', help_text='cm')
    tree_height = models.FloatField(verbose_name='Altura del árbol', help_text='m',
                                    validators=[tree_height_validation])
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE, blank=True, null=True)
    phytosanitary_status = models.CharField(max_length=100,
                                            choices=PHYTOSANITARY_STATUS_CHOICES,
                                            default=BUENO)
    sociological_classification = models.CharField(verbose_name='Clasificación sociologica',
                                                   max_length=100,
                                                   choices=SOCIOLOGICAL_CLASSIFICATION_CHOICES,
                                                   default=EMERGENTE)
    obs = models.TextField(verbose_name="Observaciones", blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Medición de árbol'
        verbose_name_plural = 'Mediciones de árboles'

    def __str__(self):
        return f'{self.tree.tree_id}; {self.field.date}'

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:tree_measurement_detail', kwargs={'pk': self.pk})
