from django.contrib import admin

from sysimibio.bibliography.forms import PublicationForm, UploadSpeciesListForm
from sysimibio.bibliography.models import Publication, SpeciesList, OccurrenceList


class PublicationAdmin(admin.ModelAdmin):
    form = PublicationForm

class SpeciesListForm(admin.ModelAdmin):
    form = UploadSpeciesListForm


admin.site.register(Publication, PublicationAdmin)
admin.site.register(SpeciesList, SpeciesListForm)
admin.site.register(OccurrenceList)
