from django.db import models
from djgeojson.fields import PointField
# Create your models here.
# todo crear metodo get_absolut link


class BioblitzProject(models.Model):
    iconURL = models.URLField(verbose_name="URL del icono del proyecto", blank=True)
    description = models.TextField(verbose_name="Descripción del proyecto", blank=True)
    created_at = models.DateTimeField(verbose_name="Fecha de creacción")
    title = models.CharField(verbose_name="Título del proyecto", max_length=200)
    project_id = models.IntegerField(verbose_name="Id del proyecto", unique=True)
    project_slug = models.CharField(verbose_name="Slug del proyecto", max_length=250)
    place_id = models.IntegerField(verbose_name="Id del local", unique=True)
    project_type = models.CharField(verbose_name="Tipo de proyecto", max_length=100)
    manager_id = models.IntegerField(verbose_name="Id del administrador", unique=True)
    manager_login = models.CharField(verbose_name="Login del administrador", max_length=200)
    manager_name = models.CharField(verbose_name="Nombre del administrador", max_length=200)

    def __str__(self):
        return f'{self.title} {self.manager_name} {self.project_id}'


    class Meta:
        verbose_name = "Proyecto de BioBlitz"
        verbose_name_plural = "Proyecto de BioBlitz"


class BioblitzOccurrence(models.Model):
    proj_id = models.ForeignKey("BioBlitzProject", on_delete=models.CASCADE) # todo melhorar nombre
    obs_id = models.IntegerField("ID de la observación")
    quality_grade = models.CharField("Calidad de ranking", max_length=50)
    created_at = models.DateTimeField("Fecha de la observación")
    uri = models.URLField("URL de la observación")
    # taxon
    name = models.CharField("Nombre cientifico de la especie", max_length=300)
    rank = models.CharField("Ranking taxonomico", max_length=50)
    iconic_taxon_name = models.CharField("Ranking taxonomico", max_length=50)
    endemic = models.BooleanField("Especie endémica?", default=False)
    threatened = models.BooleanField("Especie amenazada?", default=False)
    introduced = models.BooleanField("Especie introducida?", default=False)
    native = models.BooleanField("Especie nativa?", default=False)
    # geo
    geom = PointField()
    # User
    user_id = models.IntegerField("ID del observador")

    def __str__(self):
        return f'{self.name} - {self.proj_id}'


    class Meta:
        verbose_name = "Especie obseervada"
        verbose_name_plural = "Especies observadas"
