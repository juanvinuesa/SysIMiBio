from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sysimibio.imibio_ecological_data.forms import TreeEcologicalForm


def TreeEcologicalRegistration(request):
    if request.method == 'POST':
        form = TreeEcologicalForm(request.POST)

        if form.is_valid():
            messages.success(request, "Registro ecológico agregado con exito")
            # ImibioOccurrence.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/registro_ecologico_arboreas/')
        else:
            return render(request, 'tree_ecological_registration_form.html',
                          {'form': form})
    else:
        context = {'form': TreeEcologicalForm()}
        return render(request, 'tree_ecological_registration_form.html', context)
