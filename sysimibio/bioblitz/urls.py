from django.urls import path

from sysimibio.bioblitz.views import register_bioblitz_project, register_bioblitz_occurrences, \
    list_bioblitz_occurrences, list_bioblitz_project, bioblitz_occurrence_detail, project_detail, project_stats

app_name = 'bioblitz'


urlpatterns = [
    path('', register_bioblitz_project, name='register_bioblitz'),
    path('projects_list', list_bioblitz_project, name='list_bioblitz'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('get_occurrences/<int:pk>', register_bioblitz_occurrences, name='get_occurrences'),
    path('list_occurrences/', list_bioblitz_occurrences, name='list_occurrences'), # todo cambiar nombre
    path('occurrence/<int:pk>', bioblitz_occurrence_detail, name='occurrence_detail'),
    path('project_stats/', project_stats, name='project_stats'),
]
