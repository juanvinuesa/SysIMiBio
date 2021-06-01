from django.urls import path

from sysimibio.bibliography.views import publication_new, publication_detail, publication_list, publication_edit

app_name = 'bibliography'

urlpatterns = [
    path('new/', publication_new, name='publication_new'),
    path('detail/<int:pk>/', publication_detail, name='publication_detail'),
    path('list/', publication_list, name='publication_list'),
    path('edit/<int:pk>/', publication_edit, name='publication_edit'),
]
