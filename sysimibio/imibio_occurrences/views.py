from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sysimibio.imibio_occurrences.forms import OccurrencesRegistrationForm
from sysimibio.imibio_occurrences.models import ImibioOccurrence


def registration(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = OccurrencesRegistrationForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Formulário con error: revise todos los campos')
        return render(request, 'occurrences/occurrences_registration_form.html',
                      {'form': form})

    messages.success(request, "Registro realizado con exito")
    ImibioOccurrence.objects.create(**form.cleaned_data)
    return HttpResponseRedirect('/registro_ocurrencias/')

def new(request):
    return render(request, 'occurrences/occurrences_registration_form.html', {'form': OccurrencesRegistrationForm()})
