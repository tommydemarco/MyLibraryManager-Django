from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

#from .models import Book, Category

from django.contrib import messages

from django.urls import reverse_lazy


#users view
class HomeView(TemplateView):
    template_name = 'user/home.html'

class ContactSupportView(TemplateView):
    template_name = 'user/contact-support.html'