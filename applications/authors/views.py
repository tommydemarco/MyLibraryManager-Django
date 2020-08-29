from django.shortcuts import render

from django.views.generic import ListView

from .models import Author 

#authors view
class ListAuthorsView(ListView):
    template_name = 'authors/list.html'
    model = Author
    context_object_name = 'authors'