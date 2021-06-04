from django.contrib import messages
from django.db.models import Count
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
            return render(request, 'bioblitz/project_registration_form.html',
                          {'form': form})
        bioblitz_project_data = get_projects(q=form.cleaned_data.get("project_slug"), member_id=1626810) # todo crear view especifica con validacion

        if bioblitz_project_data.get("total_results") == 0:
            messages.error(request, 'Proyecto no encontrado. confirmar nombre o id')
            return render(request, 'bioblitz/project_registration_form.html',
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

        return HttpResponseRedirect(r('bioblitz:project_detail', project.pk))

    return render(request, 'bioblitz/project_registration_form.html', {'form': BioblitzModelForm()})

def list_bioblitz_project(request):
    ptojects = BioblitzProject.objects.all()
    return render(request, 'bioblitz/projects_list.html', {'projects': ptojects})

def project_detail(request, pk):
    try:
        project = BioblitzProject.objects.get(pk=pk)
    except BioblitzProject.DoesNotExist:
        raise Http404

    return render(request, 'bioblitz/project_detail.html', {'project': project})

def register_bioblitz_occurrences(request, pk):
    try:
        project = BioblitzProject.objects.get(project_id=pk)
        observations = get_observations(project_id=project.project_id, page = 2) # todo work on accessing all observations using len(obs.get("results"))
        # todo consider user_agent https://pyinaturalist.readthedocs.io/en/v0.13.0/general_usage.html#user-agent
        total_obs = len(observations.get("results"))
        for obs in observations.get("results"):
            print(obs.get("id"))
            project_id = project
            obs_id = obs.get('id')
            quality_grade = obs.get("quality_grade")
            created_at = obs.get('created_at')
            uri = obs.get('uri')
            geom = obs.get('geojson', '')
            # taxon
            name = obs.get('taxon').get('name')
            rank = obs.get('taxon').get('rank')
            iconic_taxon_name = obs.get('taxon').get('iconic_taxon_name')
            endemic = obs.get('taxon').get('endemic')
            threatened = obs.get('taxon').get('threatened')
            introduced = obs.get('taxon').get('introduced')
            native = obs.get('taxon').get('native')
            # user
            user_login = obs.get('user').get("login")
            user_name = obs.get('user').get("name")
            user_id = obs.get('user').get("id")

            BioblitzOccurrence.objects.create(
                project_id = project_id,
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
                native=native,
                geom = geom,
                user_id = user_id,
                user_name = user_name,
                user_login = user_login
            )

        messages.success(request, f"{total_obs} observaciones cargadas con exito")
        return HttpResponseRedirect(r('bioblitz:list_occurrences'))

    except BioblitzProject.DoesNotExist:
        raise Http404

def list_bioblitz_occurrences(request):
    observations = BioblitzOccurrence.objects.all()
    return render(request, 'bioblitz/occurrences_list.html', {'observations': observations})

def bioblitz_occurrence_detail(request, pk):
    try:
        observation = BioblitzOccurrence.objects.get(pk=pk)
    except BioblitzProject.DoesNotExist:
        raise Http404
    return render(request, 'bioblitz/occurrence_detail.html', {'observation': observation})

def project_stats(request):
    # Observations
    labelsObsQGrade = []
    dataObsQGrade = []
    labelsObsRank = []
    dataObsRank = []
    labelsObsITName = []
    dataObsITName = []
    labelsObsUser = []
    dataObsUser = []

    # Species
    labelsSppQGrade = []
    dataSppQGrade = []
    labelsSppRank = []
    dataSppRank = []
    labelsSppITName = []
    dataSppITName = []
    labelsSppUser = []
    dataSppUser = []

    # return object
    data = dict()
    labels = dict()

    # Observation
    # quality grade
    querysetGrade = BioblitzOccurrence.objects.values('quality_grade').annotate(Count('obs_id'))
    for QGrade in querysetGrade:
        labelsObsQGrade.append(QGrade.get('quality_grade'))
        dataObsQGrade.append(QGrade.get('obs_id__count'))

    data["ObsQGrade"] = dataObsQGrade
    labels["ObsQGrade"] = labelsObsQGrade

    # Rank
    querysetRank = BioblitzOccurrence.objects.values('rank').annotate(Count('obs_id'))
    for rank in querysetRank:
        labelsObsRank.append(rank.get('rank'))
        dataObsRank.append(rank.get('obs_id__count'))

    data["ObsRank"] = dataObsRank
    labels["ObsRank"] = labelsObsRank

    # ITName
    querysetITName = BioblitzOccurrence.objects.values('iconic_taxon_name').annotate(Count('obs_id'))
    for ITName in querysetITName:
        labelsObsITName.append(ITName.get('iconic_taxon_name'))
        dataObsITName.append(ITName.get('obs_id__count'))

    data["ObsITName"] = dataObsITName
    labels["ObsITName"] = labelsObsITName

    # User_id
    querysetUser = BioblitzOccurrence.objects.values('user_login').annotate(Count('obs_id')).order_by('-obs_id__count')
    for user in querysetUser:
        labelsObsUser.append(user.get('user_login'))
        dataObsUser.append(user.get('obs_id__count'))

    data["ObsUser"] = dataObsUser
    labels["ObsUser"] = labelsObsUser

    # species
    # quality grade
    querysetGradeSpp = BioblitzOccurrence.objects.values('quality_grade').annotate(Count('name', distinct=True))
    for QGradeSpp in querysetGradeSpp:
        labelsSppQGrade.append(QGradeSpp.get('quality_grade'))
        dataSppQGrade.append(QGradeSpp.get('name__count'))

    data["SppQGrade"] = dataSppQGrade
    labels["SppQGrade"] = labelsSppQGrade

    # Rank
    querysetRankSpp = BioblitzOccurrence.objects.values('rank').annotate(Count('name', distinct=True))
    for rankSpp in querysetRankSpp:
        labelsSppRank.append(rankSpp.get('rank'))
        dataSppRank.append(rankSpp.get('name__count'))

    data["SppRank"] = dataSppRank
    labels["SppRank"] = labelsSppRank

    # ITName
    querysetITNameSpp = BioblitzOccurrence.objects.values('iconic_taxon_name').annotate(Count('name', distinct=True))
    for ITNameSpp in querysetITNameSpp:
        labelsSppITName.append(ITNameSpp.get('iconic_taxon_name'))
        dataSppITName.append(ITNameSpp.get('name__count'))

    data["SppITName"] = dataSppITName
    labels["SppITName"] = labelsSppITName

    # User_id
    querysetUserSpp = BioblitzOccurrence.objects.values('user_login').annotate(Count('name', distinct=True)).order_by('-name__count')
    for userSpp in querysetUserSpp:
        labelsSppUser.append(userSpp.get('user_login'))
        dataSppUser.append(userSpp.get('name__count'))

    data["SppUser"] = dataSppUser
    labels["SppUser"] = labelsSppUser

    return render(request, 'bioblitz/project_stats.html', {
        'labels': labels,
        'data': data,
    })

