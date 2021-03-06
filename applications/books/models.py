from django.db import models

#importing the author model
from applications.authors.models import Author

#importing the manager
from .managers import BookManager

# books models

#category
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category_name}'

#book info
class Book(models.Model):
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, default=2)
    date_published = models.DateField(auto_now_add=False)
    #book_cover = models.ImageField(upload_to='covers')
    book_description = models.TextField(max_length=600)

    #connecting the manager class
    objects = BookManager()

    def __str__(self):
        author_list = self.book_author.all()
        author_list = list(author_list)
        return f'{self.book_title}'

