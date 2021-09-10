from django.views.generic import ListView, DetailView, UpdateView, CreateView
from djgeojson.views import GeoJSONLayerView

# from django.utils.decorators import method_decorator # todo usar @method_decorator(login_required)
from sysimibio.imibio_tree_ecological_data.forms import TreeForm, FieldForm, PermanentParcelForm, TreeMeasurementForm
from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, PermanentParcel, TreeMeasurement


class PlotCreateView(CreateView):
    model = PermanentParcel
    form_class = PermanentParcelForm


PlotCreateView = PlotCreateView.as_view()


class PlotEditView(UpdateView):
    model = PermanentParcel
    form_class = PermanentParcelForm


PlotEditView = PlotEditView.as_view()


class PlotListView(ListView):
    model = PermanentParcel


PlotListView = PlotListView.as_view()


class PlotDetailView(DetailView):
    model = PermanentParcel


PlotDetailView = PlotDetailView.as_view()


class PlotDetailGeoJson(GeoJSONLayerView):
    model = PermanentParcel
    properties = ('popup_content',)

    def get_queryset(self):
        self.plot = super().get_queryset()
        # self.plot = get_object_or_404(PermanentParcel, pk=self.kwargs['pk'])
        return self.plot.filter(pk=self.kwargs['pk'])


PlotDetailGeoJson = PlotDetailGeoJson.as_view()


class FieldWorkCreateView(CreateView):
    model = FieldWork
    form_class = FieldForm


FieldWorkCreateView = FieldWorkCreateView.as_view()


class FieldWorkEditView(UpdateView):
    model = FieldWork
    form_class = FieldForm


FieldWorkEditView = FieldWorkEditView.as_view()


class FieldWorkListView(ListView):
    model = FieldWork


FieldWorkListView = FieldWorkListView.as_view()


class FieldWorkDetailView(DetailView):
    model = FieldWork


FieldWorkDetailView = FieldWorkDetailView.as_view()


class TreeCreateView(CreateView):
    model = Tree
    form_class = TreeForm


TreeCreateView = TreeCreateView.as_view()


class TreeEditView(UpdateView):
    model = Tree
    form_class = TreeForm


TreeEditView = TreeEditView.as_view()


class TreeListView(ListView):
    model = Tree


TreeListView = TreeListView.as_view()


class TreeDetailView(DetailView):
    model = Tree


TreeDetailView = TreeDetailView.as_view()


class TreeDetailGeoJson(GeoJSONLayerView):
    model = Tree
    properties = ('popup_content',)

    def get_queryset(self):
        self.tree = super().get_queryset()
        return self.tree.filter(pk=self.kwargs['pk'])


TreeDetailGeoJson = TreeDetailGeoJson.as_view()


class TreeMeasurementCreateView(CreateView):
    model = TreeMeasurement
    form_class = TreeMeasurementForm


TreeMeasurementCreateView = TreeMeasurementCreateView.as_view()


class TreeMeasurementEditView(UpdateView):
    model = TreeMeasurement
    form_class = TreeMeasurementForm


TreeMeasurementEditView = TreeMeasurementEditView.as_view()


class TreeMeasurementListView(ListView):
    model = TreeMeasurement
    ordering = ['-created_at']


TreeMeasurementListView = TreeMeasurementListView.as_view()


class TreeMeasurementDetailView(DetailView):
    model = TreeMeasurement


TreeMeasurementDetailView = TreeMeasurementDetailView.as_view()


class TreesGeoJson(GeoJSONLayerView):
    model = Tree
    properties = ('popup_content',)


trees_geojson = TreesGeoJson.as_view()
