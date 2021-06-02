from django.urls import path

from sysimibio.imibio_tree_ecological_data.views import new, detail

app_name = 'imibio_tree_ecological_data'
# todo crear lista de spp por parcela
# todo crear lista spp por campo
urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
    # path('geojson/', trees_geojson, name='data'),
]
