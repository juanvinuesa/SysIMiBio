from django.db import models

# Create your models here.

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
