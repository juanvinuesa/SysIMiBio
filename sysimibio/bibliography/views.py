from crossref.restful import Works
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from isbnlib import is_isbn13, meta
from django.urls import reverse


from sysimibio.bibliography.forms import PublicationForm
from sysimibio.bibliography.models import Publication


class PublicationUpdateClass(LoginRequiredMixin, UpdateView):
    model = Publication
    form_class = PublicationForm

    def get_success_url(self):
        objectid = self.kwargs['pk']
        return reverse('bibliography:publication_detail', kwargs={'pk': objectid})


PublicationUpdateView = PublicationUpdateClass.as_view()


class PublicationListClass(LoginRequiredMixin, ListView):
    model = Publication
    context_object_name = 'publications'
    ordering = ['-publication_year']


PublicationList = PublicationListClass.as_view()


class PublicationDetailClass(LoginRequiredMixin, DetailView):
    model = Publication


PublicationDetail = PublicationDetailClass.as_view()


class PublicationCreateClass(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm

    def form_valid(self, form):
        self.publication = form.save(commit=False)
        self.publication.created_by = self.request.user
        works = Works()
        if self.publication.DOI != "" and works.doi_exists(self.publication.DOI):
            paper_data_result = works.doi(self.publication.DOI)
            self.publication.publication_year = str(paper_data_result.get('created').get('date-parts')[0][0])
            self.publication.title = paper_data_result.get('title')[0]
            self.publication.author = f"{paper_data_result.get('author')[0].get('given')},{paper_data_result.get('author')[0].get('family')}"
            sub = paper_data_result.get("subject", [self.publication.subject]) #todo ver si puede mejorar en una linea
            self.publication.subject = ', '.join([str(elem) for elem in sub])
            self.publication.URL = paper_data_result.get('URL')

        elif self.publication.ISBN != "" and is_isbn13(self.publication.ISBN):
            book_data_result = meta(self.publication.ISBN)
            self.publication.publication_year = book_data_result.get('Year')
            self.publication.title = book_data_result.get('Title')
            self.publication.author = book_data_result.get('Authors')[0]

        elif self.publication.crossref and (self.publication.DOI or self.publication.ISBN):
            messages.error(self.request, 'DOI/ISBN no encontrado. Cargar datos y desmarcar el campo "tiene DOI/ISBN"')
            return render(self.request, 'bibliography/publication_form.html', {'form': form})
        self.publication.save()
        messages.success(self.request, "Registro realizado con exito")

        return redirect('bibliography:publication_detail', pk=self.publication.pk)


PublicationCreateView = PublicationCreateClass.as_view()
