from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "books"

urlpatterns = [
    #list views
    path('', views.ListBooksView.as_view(), name="books"),
    #create views
    path('add-new/', views.AddNewBook.as_view(), name="add_new"),
]

