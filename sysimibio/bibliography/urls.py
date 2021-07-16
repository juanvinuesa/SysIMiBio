from django.urls import path

from sysimibio.bibliography.views import PublicationList, \
    PublicationDetail, Publication_UpdateView, PublicationCreateView

app_name = 'bibliography'

urlpatterns = [
    path('new/', PublicationCreateView, name='publication_new'),
    path('detail/<int:pk>/', PublicationDetail, name='publication_detail'),
    path('list/', PublicationList, name='publication_list'),
    path('edit/<int:pk>/', Publication_UpdateView, name='publication_edit'),
]
