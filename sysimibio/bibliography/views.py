from crossref.restful import Works
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, resolve_url as r
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from isbnlib import is_isbn13, meta

from sysimibio.bibliography.forms import PublicationForm, UploadSpeciesListForm, UpdateSpeciesListForm
from sysimibio.bibliography.models import Publication, SpeciesList


class PublicationUpdateClass(LoginRequiredMixin, UpdateView):
    model = Publication
    form_class = PublicationForm

    def get_success_url(self):
        objectid = self.kwargs['pk']
        return r('bibliography:publication_detail', objectid)


PublicationUpdateView = PublicationUpdateClass.as_view()


class PublicationListClass(LoginRequiredMixin, ListView):
    model = Publication
    context_object_name = 'publications'
    ordering = ['-publication_year']


PublicationList = PublicationListClass.as_view()


class PublicationDetailClass(LoginRequiredMixin, DetailView):
    model = Publication

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['species_list'] = SpeciesList.objects.filter(bibliography=self.kwargs['pk'])
        return context


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
            sub = paper_data_result.get("subject", [self.publication.subject])  # todo ver si puede mejorar en una linea
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


def handle_uploaded_species_list_file(file, publication_pk):
    import pandas as pd
    df = pd.read_csv(file)  # todo confirmar si funcion anda bien con solo una columna, felipe
    columns_sequence = [number for number in range(1, len(df.columns))]
    result = pd.DataFrame()
    result[
        "scientific_name"] = df.scientific_name  # todo como gneralizar eso para que sea la primera columna independiente de su nombre felipe
    result["bibliography"] = Publication.objects.get(pk=publication_pk)
    result = result.join(
        pd.DataFrame({"other_fields_json": df.iloc[:, columns_sequence].to_dict("records")}))
    return result


# def upload_specieslist(request):
#     if request.method == 'POST':
#         form = UploadSpeciesListForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             uploaded_file = request.FILES['species_list_spreadsheet'],
#             publication_pk = request.POST["bibliography"]
#             df = handle_uploaded_species_list_file(
#                 file=uploaded_file[0],
#                 publication_pk=publication_pk)
#             SpeciesList.objects.bulk_create(
#                 SpeciesList(**vals) for vals in df.to_dict('records'))
#             return HttpResponseRedirect(r('bibliography:publication_detail',
#                                           publication_pk))
#         else:
#             return render(request, 'bibliography/specieslist_form.html', {'form': form})
#     else:
#         form = UploadSpeciesListForm()
#         return render(request, 'bibliography/specieslist_form.html',
#                       {'form': form})


class SpeciesListCreateClass(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = UpdateSpeciesListForm

    def post(self, request, *args, **kwargs):
        form = UploadSpeciesListForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['species_list_spreadsheet'],
            publication_pk = request.POST["bibliography"]
            df = handle_uploaded_species_list_file(
                file=uploaded_file[0],
                publication_pk=publication_pk)
            SpeciesList.objects.bulk_create(
                SpeciesList(**vals) for vals in df.to_dict('records'))
            return HttpResponseRedirect(r('bibliography:publication_detail',
                                          publication_pk))
        else:
            return render(request, 'bibliography/specieslist_form.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UploadSpeciesListForm()
        return render(request, 'bibliography/specieslist_form.html',
                      {'form': form})


SpeciesListCreateView = SpeciesListCreateClass.as_view()


class SpeciesListUpdateClass(LoginRequiredMixin, UpdateView):
    model = Publication
    form_class = UpdateSpeciesListForm

    def post(self, request, *args, **kwargs):
        form = UpdateSpeciesListForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['species_list_spreadsheet'],
            publication_pk = request.POST["bibliography"]
            species_to_update = SpeciesList.objects.filter(bibliography=publication_pk)
            df = handle_uploaded_species_list_file(
                file=uploaded_file[0],
                publication_pk=publication_pk)
            dict_list = [row for row in df.to_dict('records')]
            for index, obj in enumerate(list(species_to_update)):
                dato = dict_list[index]
                for key, value in dato.items():
                    setattr(obj, key, value)
            SpeciesList.objects.bulk_update(
                species_to_update,
                ['scientific_name', 'other_fields_json'])
            return HttpResponseRedirect(r('bibliography:publication_detail',
                                          publication_pk))
        else:
            return render(request, 'bibliography/specieslist_form.html', {'form': form})

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        form = UpdateSpeciesListForm()
        form.fields["bibliography"].queryset = Publication.objects.filter(pk=pk)
        return render(request, 'bibliography/specieslist_form.html',
                      {'form': form})


SpeciesListUpdateView = SpeciesListUpdateClass.as_view()
