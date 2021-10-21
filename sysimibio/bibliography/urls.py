from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from sysimibio.bibliography.views import PublicationList, \
    PublicationDetail, PublicationUpdateView, PublicationCreateView, \
    SpeciesListUpdateView, SpeciesListCreateView, OccurrenceListCreateView, OccurrenceListUpdateView

app_name = 'bibliography'

urlpatterns = [
    path('new/', PublicationCreateView, name='publication_new'),
    path('detail/<int:pk>/', PublicationDetail, name='publication_detail'),
    path('list/', PublicationList, name='publication_list'),
    path('edit/<int:pk>/', PublicationUpdateView, name='publication_edit'),
    path('new/specieslist/<int:pk>/', SpeciesListCreateView, name='specieslist_new'),
    path('edit/specieslist/<int:pk>/', SpeciesListUpdateView, name='specieslist_edit'),
    path('new/occurrenceslist/<int:pk>/', OccurrenceListCreateView, name='occurrenceslist_new'),
    path('edit/occurrenceslist/<int:pk>/', OccurrenceListUpdateView, name='occurrenceslist_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)