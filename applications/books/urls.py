from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "books"

urlpatterns = [
    #list views
    path('', views.ListBooksView.as_view(), name="books"),
    #detail views 
    path('book-details/<pk>', views.BookDetailsView.as_view(), name="book_details"),
    #edit view 
    path('edit-book-details/<pk>', views.EditBookDetailsView.as_view(), name="edit_book_details"),
    #create views
    path('add-new/', views.AddNewBook.as_view(), name="add_new"),
]

