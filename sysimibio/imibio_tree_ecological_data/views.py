from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, resolve_url as r
from sysimibio.imibio_tree_ecological_data.forms import TreeEcologicalForm
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree


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
    return render(request, 'tree_ecological_registration_form.html', {'form': TreeEcologicalForm()})


def create(request):
    form = TreeEcologicalForm(request.POST)

    if not form.is_valid():
        return render(request, 'tree_ecological_registration_form.html',
                      {'form': form})

    tree_eco_data = TreeEcologicalData.objects.create(**form.cleaned_data)
    messages.success(request, "Registro ecológico agregado con exito")
    return HttpResponseRedirect(r('imibio_tree_ecological_data:detail', tree_eco_data.pk))
