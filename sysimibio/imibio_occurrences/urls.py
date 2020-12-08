from django.urls import path

from sysimibio.imibio_occurrences.views import registration

app_name = 'imibio_occurrences'

urlpatterns = [
    path('', registration, name='new'),
]
