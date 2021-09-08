from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from djgeojson.views import GeoJSONLayerView

# from django.utils.decorators import method_decorator # todo usar @method_decorator(login_required)
from sysimibio.imibio_tree_ecological_data.forms import TreeForm, FieldForm, PermanentParcelForm, TreeMeasurementForm
from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, PermanentParcel, TreeMeasurement
from django.views.generic import ListView, DetailView, UpdateView, CreateView


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


# class TreeEditView(UpdateView):
#     model = Tree
#     form_class = TreeForm
#
#
# TreeEditView = TreeEditView.as_view()


# class TreeListView(ListView):
#     model = Tree
#
#
# TreeListView = TreeListView.as_view()


class TreeMeasurementDetailView(DetailView):
    model = TreeMeasurement


TreeMeasurementDetailView = TreeMeasurementDetailView.as_view()


# class TreeMeasurementDetailGeoJson(GeoJSONLayerView):
#     model = TreeMeasurement
#     properties = ('popup_content',)
#
#     def get_queryset(self):
#         self.tree_measurement = super().get_queryset()
#         return self.tree_measurement.filter(pk=self.kwargs['pk'])


# TreeDetailGeoJson = TreeDetailGeoJson.as_view()

def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def detail(request, pk):
    try:
        tree_detail = Tree.objects.get(pk=pk)
    except Tree.DoesNotExist:
        raise Http404
    return render(request, 'tree_ecological_detail.html',
                  {'tree_detail': tree_detail})


def empty_form(request):
    context = {'form': TreeForm(),
               'fieldForm': FieldForm()}
    return render(request, 'tree_ecological_registration_form.html', context) # todo considerar Fieldwork form


def create(request):
    form = TreeForm(request.POST)

    if not form.is_valid():
        return render(request, 'tree_ecological_registration_form.html',
                      {'form': form})

    tree_eco_data = FieldWork.objects.create(**form.cleaned_data)
    messages.success(request, "Registro ecológico agregado con exito")
    return HttpResponseRedirect(r('imibio_tree_ecological_data:detail', tree_eco_data.pk))


class TreesGeoJson(GeoJSONLayerView):
    model = Tree
    properties = ('popup_content',)


trees_geojson = TreesGeoJson.as_view()
