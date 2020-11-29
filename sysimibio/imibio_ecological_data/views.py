from django.shortcuts import render
from sysimibio.imibio_ecological_data.forms import TreeEcologicalForm


def TreeEcologicalRegistration(request):
    context = {'form': TreeEcologicalForm()}
    return render(request, 'tree_ecological_registration_form.html', context)
