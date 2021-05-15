from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from pyinaturalist.node_api import get_projects


# Create your views here.
from sysimibio.bioblitz.forms import BioblitzModelForm
from sysimibio.bioblitz.models import BioblitzProject # todo cambiar a singular


def register_bioblitz_project(request):
    if request.method == 'POST':
        form = BioblitzModelForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Formulário con error: revise todos los campos')
            return render(request, 'bioblitz/bioblitz_registration_form.html',
                          {'form': form})
        print(form.cleaned_data.get("project_slug"))
        bioblitz_project_data = get_projects(q=form.cleaned_data.get("project_slug"))
        print(bioblitz_project_data.keys())
        print(bioblitz_project_data.get("total_results"))
        if bioblitz_project_data.get("total_results") == 0:
            messages.error(request, 'Proyecto no encontrado. confirmar nombre o id')
            return render(request, 'bioblitz/bioblitz_registration_form.html',
                          {'form': form})

        project = BioblitzProject.objects.create(
            iconURL= bioblitz_project_data.get("results")[0].get('icon'),
            description = bioblitz_project_data.get("results")[0].get('description'),
            created_at = bioblitz_project_data.get("results")[0].get('created_at'),
            title = bioblitz_project_data.get("results")[0].get('title'),
            project_id = bioblitz_project_data.get("results")[0].get('id'),
            project_slug = bioblitz_project_data.get("results")[0].get('slug'),
            place_id = bioblitz_project_data.get("results")[0].get('place_id'),
            project_type = bioblitz_project_data.get("results")[0].get('project_type'),
            manager_id = bioblitz_project_data.get("results")[0].get('admins')[0].get("user").get("id"),
            manager_login = bioblitz_project_data.get("results")[0].get('admins')[0].get("user").get("login"),
            manager_name = bioblitz_project_data.get("results")[0].get('admins')[0].get("user").get("name")
        )
        messages.success(request, "Proyecto registrado con exito")

        return HttpResponseRedirect(r('bioblitz:detail', project.pk))

    return render(request, 'bioblitz/bioblitz_registration_form.html', {'form': BioblitzModelForm()})


def detail(request, pk):
    try:
        project = BioblitzProject.objects.get(pk=pk)
    except BioblitzProject.DoesNotExist:
        raise Http404

    return render(request, 'bioblitz/bioblitz_detail.html', {'project': project})

