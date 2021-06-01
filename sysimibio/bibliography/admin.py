from django.contrib import admin

from sysimibio.bibliography.forms import PublicationForm
from sysimibio.bibliography.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    form=PublicationForm

admin.site.register(Publication, PublicationAdmin)