from django.urls import path

from sysimibio.bioblitz.views import bioblitz

app_name = 'bioblitz'


urlpatterns = [
    path('', bioblitz, name='bioblitz'),
]
