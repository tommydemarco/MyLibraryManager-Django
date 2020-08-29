from django.shortcuts import render

from django.views.generic import ListView

from .models import Author 

#authors view
class ListAuthorsView(ListView):
    template_name = 'authors/list.html'
    context_object_name = 'authors'

    def get_queryset(self):

        #for an author search, getting the name from the form
        name = self.request.GET.get("name", "")
        surname = self.request.GET.get("surname", "")

        if name:
            return Author.objects.search_author_by_name(name)
        elif surname:
            return Author.objects.search_author_by_surname(surname)

        #using the function of the manager to return the QuerySet
        return Author.objects.list_authors()