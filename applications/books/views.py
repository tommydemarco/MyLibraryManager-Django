from django.shortcuts import render

from django.views.generic import ListView

from .models import Book, Category

from django.contrib import messages

#books view
class ListBooksView(ListView):
    template_name = 'books/list.html'
    context_object_name = 'books'

    def get_queryset(self):

        #for an author search, getting the name from the form
        date_published1 = self.request.GET.get("date1", "")
        date_published2 = self.request.GET.get("date2", "")

        if date_published1 and date_published2:
            return Book.objects.search_books_by_date_published(date_published1, date_published2)

        #using the function of the manager to return the QuerySet
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context["categories"] = Category.objects.all()
        return context