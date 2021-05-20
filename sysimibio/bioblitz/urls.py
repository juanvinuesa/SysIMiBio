from django.urls import path

from sysimibio.bioblitz.views import register_bioblitz_project, register_bioblitz_occurrences, \
    list_bioblitz_occurrences, list_bioblitz_project, bioblitz_occurrence_detail, project_detail, group_pie_chart

app_name = 'bioblitz'


urlpatterns = [
    path('', register_bioblitz_project, name='register_bioblitz'),
    path('projects_list', list_bioblitz_project, name='list_bioblitz'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('get_occurrences/<int:pk>', register_bioblitz_occurrences, name='get_occurrences'),
    path('list_occurrences/', list_bioblitz_occurrences, name='list_occurrences'),
    path('occurrence/<int:pk>', bioblitz_occurrence_detail, name='occurrence_detail'),
    path('pie-chart/', group_pie_chart, name='pie-chart'),
    # path('user_bar-chart/', user_bar_chart, name='user-bar-chart'),
]
