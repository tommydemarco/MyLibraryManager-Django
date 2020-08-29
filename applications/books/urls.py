from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "books"

urlpatterns = [
    path('', views.ListBooksView.as_view(), name="books"),
]

