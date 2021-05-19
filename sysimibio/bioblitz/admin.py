from django.contrib import admin
from sysimibio.bioblitz.models import BioblitzProject, BioblitzOccurrence
# Register your models here.

admin.site.register(BioblitzProject)
admin.site.register(BioblitzOccurrence)
