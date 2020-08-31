from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import Author 

from django.contrib import messages

from django.urls import reverse_lazy

from .forms import AddAuthor

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


#create new book
class AddNewAuthor(CreateView):
    template_name = "authors/create.html"
    model = Author
    
    #inserting a form class for the form
    form_class = AddAuthor

    #adding the url for when the process is complete.
    #required in a CreateView
    #syntax: 'urls_app_name:url_name'
    success_url = reverse_lazy('authors:authors')

    #THE FORM VALID  TAKES PLACE AFTER THE FORM HAS BEEN VALIDATED
    #adding attributes automatically using the method form_valid
    def form_valid(self, form):
        #saving the information submitted
        # employee = form.save()
        # #making the new attruibute to the new instance
        # employee.full_name = employee.first_name + ' ' + employee.last_name
        # #saving the outcome
        # employee.save()

        success_message = messages.add_message(self.request, messages.SUCCESS, 
        'The new author has been successfully added to the database. You have been redirected to the book list')
        #syntax for returning the result  of the form valid
        return super(AddNewAuthor, self).form_valid(form)