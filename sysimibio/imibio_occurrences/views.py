from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sysimibio.imibio_occurrences.forms import OccurrencesRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = OccurrencesRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registro realizado con exito")
            return HttpResponseRedirect('/registro_ocurrencias/')
        else:
            return render(request, 'occurrences/occurrences_registration_form.html',
                          {'form': form})
    else:
        context ={'form': OccurrencesRegistrationForm()}
        return render(request, 'occurrences/occurrences_registration_form.html', context)