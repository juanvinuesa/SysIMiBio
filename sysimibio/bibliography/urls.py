from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from sysimibio.bibliography.views import PublicationList, \
    PublicationDetail, PublicationUpdateView, PublicationCreateView, upload_specieslist, \
    SpeciesListUpdateView, SpeciesListCreateView

app_name = 'bibliography'

urlpatterns = [
    path('new/', PublicationCreateView, name='publication_new'),
    path('detail/<int:pk>/', PublicationDetail, name='publication_detail'),
    path('list/', PublicationList, name='publication_list'),
    path('edit/<int:pk>/', PublicationUpdateView, name='publication_edit'),
    path('new/specieslist/', SpeciesListCreateView, name='species_new'),
    path('edit/specieslist/<int:pk>/', SpeciesListUpdateView, name='specieslist_edit'),

    # path('list/specieslist/', Species_List, name='species_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)