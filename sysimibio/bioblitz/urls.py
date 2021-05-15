from django.urls import path

from sysimibio.bioblitz.views import register_bioblitz_project, detail

app_name = 'bioblitz'


urlpatterns = [
    path('', register_bioblitz_project, name='bioblitz'),
    path('<int:pk>/', detail, name='detail'),
]
