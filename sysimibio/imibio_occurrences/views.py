from django.shortcuts import render
from sysimibio.imibio_occurrences.forms import OccurrencesRegistrationForm


def registration(request):
    context ={'form': OccurrencesRegistrationForm()}
    return render(request, 'occurrences/occurrences_registration_form.html', context)