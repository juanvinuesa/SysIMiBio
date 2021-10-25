from django.db.models import Q
# from django.db import models
import django_filters
from sysimibio.bibliography.models import Publication

class PublicationFilters(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', label="Definir filtro ")
    # publication_year
    # DOI
    # ISBN
    # ORCID
    # created_at
    # imibio
    # crossref
    class Meta:
        model = Publication
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Publication.objects.filter(
            Q(title__icontains=value) | Q(author__icontains=value) | Q(subject__icontains=value) | Q(observations__icontains=value)
        )
# todo add outros campos en el filtro