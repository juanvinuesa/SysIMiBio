from django.urls import path

from sysimibio.bioblitz.views import register_bioblitz_project, register_bioblitz_occurrences, \
    list_bioblitz_occurrences, list_bioblitz_project, bioblitz_occurrence_detail, project_detail, project_stats, \
    inatobs_geojson, occ_geojson

app_name = 'bioblitz'


urlpatterns = [
    path('', register_bioblitz_project, name='register_bioblitz'),
    path('projects_list', list_bioblitz_project, name='list_bioblitz'),
    path('project_detail/<int:pk>/', project_detail, name='project_detail'),
    path('project_detail/geojson/', inatobs_geojson, name='project_geojson'), # todo restringir a project_id
    path('get_occurrences/<int:project_id>/', register_bioblitz_occurrences, name='get_occurrences'),
    path('get_occurrence_geojson/<int:pk>/', occ_geojson, name='occurrence_geojson'),
    path('list_occurrences/<int:pk>/', list_bioblitz_occurrences, name='list_occurrences'), # todo cambiar nombre
    path('occurrence_detail/<int:pk>/', bioblitz_occurrence_detail, name='occurrence_detail'),
    path('project_stats/<int:pk>/', project_stats, name='project_stats'),
]
