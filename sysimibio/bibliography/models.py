from django.db import models

from sysimibio.bibliography.validators import validate_isbn


#todo una publicacion puede tener ocurrencias o lista de especies


class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    publication_year = models.CharField("Año de publicación", max_length=4, blank=True, help_text="YYYY")
    title = models.CharField('Título', max_length=255, blank=True)
    author = models.CharField('Autor', max_length=255, blank=True)
    DOI = models.CharField('DOI', max_length=30, blank=True)
    ISBN = models.CharField('ISBN', help_text='Ingresar ISBN sin guion ni puntos', max_length=13, blank=True, validators=[validate_isbn]) #todo crear un metodo clean para sacar puntos guiones
    subject = models.CharField("Palabras clave o tema", max_length=200, blank=True)
    ORCID = models.URLField("Orcid (opcional)", max_length=200, blank=True)
    URL = models.URLField("Url (opcional)", max_length=200, blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True) # todo si queres, podriamos tener un campo "create_by" como foreign key del usuario que hace el registro
    #created_by = models.ForeignKey() # todo finalizar adicionando relacion con usuario logado
    last_modification_at = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)
    observations = models.TextField(verbose_name='Observaciones', blank=True)
    imibio = models.BooleanField(verbose_name='Participación IMIBIO ?', default=False)
    crossref = models.BooleanField(verbose_name='Tiene DOI/ISBN ?',help_text='Si tiene referencias con DOI O ISBN marcar.', default=True)

    def __str__(self):
        return f'{self.author}, {self.publication_year} - {self.title}'
