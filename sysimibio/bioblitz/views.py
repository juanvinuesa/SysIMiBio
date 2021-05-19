from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from pyinaturalist.node_api import get_projects, get_observations


# Create your views here.
from sysimibio.bioblitz.forms import BioblitzModelForm
from sysimibio.bioblitz.models import BioblitzProject, BioblitzOccurrence


def register_bioblitz_project(request):
    if request.method == 'POST':
        form = BioblitzModelForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Formulário con error: revise todos los campos')
            return render(request, 'bioblitz/bioblitz_registration_form.html',
                          {'form': form})
        # print(form.cleaned_data.get("project_slug")) # todo get_projects(id=8348) o get_projects_by_id(project_id=8348)
        bioblitz_project_data = get_projects(q=form.cleaned_data.get("project_slug"), member_id=1626810)
        # print(bioblitz_project_data.keys())
        # print(bioblitz_project_data.get("total_results"))
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

        return HttpResponseRedirect(r('bioblitz:proj_detail', project.pk))

    return render(request, 'bioblitz/bioblitz_registration_form.html', {'form': BioblitzModelForm()})


def detail(request, pk):
    try:
        project = BioblitzProject.objects.get(pk=pk)
    except BioblitzProject.DoesNotExist:
        raise Http404 # todo resolver isso

    return render(request, 'bioblitz/bioblitz_detail.html', {'project': project})

def register_bioblitz_occurrences(request, pk):
    try:
        project = BioblitzProject.objects.get(project_id=pk)
        observations = get_observations(project_id=project.project_id)
        total_obs = len(observations.get("results"))
        for obs in observations.get("results"):
            print(obs.get("id"))
            obs_id = obs.get('id')
            quality_grade = obs.get("quality_grade")
            created_at = obs.get('created_at')
            uri = obs.get('uri')
            if obs.get('taxon'):
                name = obs.get('taxon').get('name')
                rank = obs.get('taxon').get('rank')
                iconic_taxon_name = obs.get('taxon').get('iconic_taxon_name')
                endemic = obs.get('taxon').get('endemic')
                threatened = obs.get('taxon').get('threatened')
                introduced = obs.get('taxon').get('introduced')
                native = obs.get('taxon').get('native')
            else:
                name = ''
                rank = ''
                iconic_taxon_name = ''
                endemic = False
                threatened = False
                introduced = False
                native = False
            BioblitzOccurrence.objects.create(
                obs_id=obs_id,
                quality_grade=quality_grade,
                created_at=created_at,
                uri=uri,
                name=name,
                rank=rank,
                iconic_taxon_name=iconic_taxon_name,
                endemic=endemic,
                threatened=threatened,
                introduced=introduced,
                native=native)

        messages.success(request, f"{total_obs} observaciones cargadas con exito")
        return HttpResponseRedirect(r('bioblitz:list_occs'))

    except BioblitzProject.DoesNotExist:
        raise Http404

def list_bioblitz_occurrences(request):
    observations = BioblitzOccurrence.objects.all()
    return render(request, 'bioblitz/occurrences_list.html', {'observations': observations})