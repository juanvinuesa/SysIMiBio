from crossref.restful import Works
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from isbnlib import is_isbn13, meta

from sysimibio.bibliography.forms import PublicationForm
from sysimibio.bibliography.models import Publication


# todo mejorar funciones....
# Podria sacarse los if de dentro.... o hacer q retornen algun valor cuando no exista.
def cross_doi(publication):
    works = Works()
    paper_data_result = works.doi(publication.DOI)
    publication.publication_year = str(paper_data_result.get('created').get('date-parts')[0][0])
    publication.title = paper_data_result.get('title')[0]
    publication.author = f"{paper_data_result.get('author')[0].get('given')},{paper_data_result.get('author')[0].get('family')}"
    publication.subject = paper_data_result.get("subject", [publication.subject])[0]
    publication.URL = paper_data_result.get('URL')


def cross_isbn(publication):
    book_data_result = meta(publication.ISBN)
    publication.publication_year = book_data_result.get('Year')
    publication.title = book_data_result.get('Title')
    publication.author = book_data_result.get('Authors')[0]


@login_required
def publication_list(request):
    publications = Publication.objects.all().order_by('-publication_year')
    return render(request, 'publication_list.html', {'publications': publications})


@login_required
def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication_detail.html', {'publication': publication})


@login_required
def publication_new(request):  # todo mejorar quebrando la view en defs distintas
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.created_by = request.user
            works = Works()
            if publication.DOI != "" and works.doi_exists(publication.DOI):
                cross_doi(publication)
            elif publication.ISBN != "" and is_isbn13(publication.ISBN):
                cross_isbn(publication)
            publication.save()
            messages.success(request, "Registro realizado con exito")

            return redirect('bibliography:publication_detail', pk=publication.pk)
        messages.error(request, 'Formulario con error: revise todos los campos')
        return render(request, 'publication_form.html', {'form': form})
    else:
        form = PublicationForm()
        return render(request, 'publication_form.html', {'form': form})


@login_required
def publication_edit(request, pk): #todo confirmar si se puede mejorar la view
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            publication.save()
            return redirect('bibliography:publication_detail', pk=publication.pk)
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'publication_form.html', {'form': form})
