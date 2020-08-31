from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import Book, Category

from django.contrib import messages

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddBook



#books view
class ListBooksView(LoginRequiredMixin, ListView):
    template_name = 'books/list.html'
    context_object_name = 'books'

    def get_queryset(self):

        #FILTER BY DATE
        #for an author search, getting the name from the form
        date_published1 = self.request.GET.get("date1", "")
        date_published2 = self.request.GET.get("date2", "")

        if date_published1 and date_published2:
            return Book.objects.search_books_by_date_published(date_published1, date_published2)

        #FILTER BY GENERE
        genere = self.request.GET.get("genere", "")

        if genere:
            return Book.objects.search_books_by_genere(genere)

        #using the function of the manager to return the QuerySet
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context["categories"] = Category.objects.all()
        return context

#create new book
class AddNewBook(LoginRequiredMixin, CreateView):
    template_name = "books/create.html"
    model = Book
    
    #inserting a form class for the form
    form_class = AddBook

    #adding the url for when the process is complete.
    #required in a CreateView
    #syntax: 'urls_app_name:url_name'
    success_url = reverse_lazy('books:books')

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
        'The book has been successfully added to the database. You have been redirected to the book list')
        #syntax for returning the result  of the form valid
        return super(CreateNewEmployee, self).form_valid(form)