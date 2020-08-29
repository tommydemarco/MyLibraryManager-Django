from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "authors"

urlpatterns = [
    path('', views.ListAuthorsView.as_view(), name="authors"),
]