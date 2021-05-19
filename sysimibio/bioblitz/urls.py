from django.urls import path

from sysimibio.bioblitz.views import register_bioblitz_project, detail, register_bioblitz_occurrences, \
    list_bioblitz_occurrences, list_bioblitz_project

app_name = 'bioblitz'


urlpatterns = [
    path('', register_bioblitz_project, name='registrar_bioblitz'),
    path('projects_list', list_bioblitz_project, name='list_bioblitz'),
    path('<int:pk>/', detail, name='proj_detail'),
    path('get_occs/<int:pk>', register_bioblitz_occurrences, name='get_occs'),
    path('list_occs/', list_bioblitz_occurrences, name='list_occs'),
]
