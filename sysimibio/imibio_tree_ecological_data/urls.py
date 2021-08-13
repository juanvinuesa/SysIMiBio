from django.urls import path
from django.views.generic import TemplateView

from sysimibio.imibio_tree_ecological_data.views import new, detail, trees_geojson, PlotListView, PlotDetailView, PlotDetailGeoJson

app_name = 'imibio_tree_ecological_data'
# todo crear lista de spp por parcela
# todo crear lista spp por campo
urlpatterns = [
    path('', new, name='new'),
    path('list/plot/', PlotListView, name='plot_list'),
    path('detail/plot/<int:pk>/', PlotDetailView, name='plot_detail'),
    path('geojson/plot/<int:pk>/', PlotDetailGeoJson, name='plot_detail_geojson'),
    path('<int:pk>/', detail, name='detail'),
    path('geojson/', trees_geojson, name='data'),
    path('map/', TemplateView.as_view(template_name='tree_map.html'), name='map'),
]
