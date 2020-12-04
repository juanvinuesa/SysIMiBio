from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sysimibio.imibio_tree_ecological_data.forms import TreeEcologicalForm
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


def TreeEcologicalRegistration(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = TreeEcologicalForm(request.POST)

    if not form.is_valid():
        return render(request, 'tree_ecological_registration_form.html',
                      {'form': form})

    TreeEcologicalData.objects.create(**form.cleaned_data)
    messages.success(request, "Registro ecológico agregado con exito")
    # ImibioOccurrence.objects.create(**form.cleaned_data)
    return HttpResponseRedirect('/registro_ecologico_arboreas/')

def new(request):
    return render(request, 'tree_ecological_registration_form.html', {'form': TreeEcologicalForm()})
