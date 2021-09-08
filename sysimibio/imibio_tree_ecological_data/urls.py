from django.urls import path
from django.views.generic import TemplateView

from sysimibio.imibio_tree_ecological_data.views import new, detail, trees_geojson, PlotListView, PlotDetailView, \
    PlotDetailGeoJson, PlotCreateView, PlotEditView, FieldWorkListView, FieldWorkDetailView, FieldWorkEditView, \
    FieldWorkCreateView, TreeCreateView, TreeDetailView, TreeDetailGeoJson, TreeEditView, TreeListView, \
    TreeMeasurementCreateView, TreeMeasurementDetailView

app_name = 'imibio_tree_ecological_data'

urlpatterns = [
    path('', new, name='new'),
    # plot
    path('create/plot/', PlotCreateView, name='plot_create'),
    path('edit/plot/<int:pk>/', PlotEditView, name='plot_edit'),
    path('list/plot/', PlotListView, name='plot_list'),
    path('detail/plot/<int:pk>/', PlotDetailView, name='plot_detail'),
    path('geojson/plot/<int:pk>/', PlotDetailGeoJson, name='plot_detail_geojson'),
    # field work
    path('create/field/', FieldWorkCreateView, name='field_create'),
    path('edit/field/<int:pk>/', FieldWorkEditView, name='field_edit'),
    path('list/field/', FieldWorkListView, name='field_list'),
    path('detail/field/<int:pk>/', FieldWorkDetailView, name='field_detail'),
    # tree
    path('create/tree/', TreeCreateView, name='tree_create'),
    path('edit/tree/<int:pk>/', TreeEditView, name='tree_edit'),
    path('list/tree/', TreeListView, name='tree_list'),
    path('detail/tree/<int:pk>/', TreeDetailView, name='tree_detail'),
    path('geojson/tree/<int:pk>/', TreeDetailGeoJson, name='Tree_detail_geojson'),
    # tree measuremnt
    path('create/tree/measurement/', TreeMeasurementCreateView, name='tree_measurement_create'),
    # path('edit/tree/<int:pk>/', TreeEditView, name='tree_edit'),
    # path('list/tree/', TreeListView, name='tree_list'),
    path('detail/tree/measurement/<int:pk>/', TreeMeasurementDetailView, name='tree_measurement_detail'),
    # path('geojson/tree/<int:pk>/', TreeDetailGeoJson, name='Tree_detail_geojson'),

    path('<int:pk>/', detail, name='detail'), # todo remove from test
    path('geojson/', trees_geojson, name='data'), # todo remove from test
    path('map/', TemplateView.as_view(template_name='tree_map.html'), name='map'), # todo remove from test
]
