from django.db import models

#importing the author model
from applications.authors.models import Author

# books models

#category
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f'Category: {self.category_name}'

#book info
class Book(models.Model):
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
    book_authors = models.ManyToManyField(Author)
    date_published = models.DateField(auto_now_add=False)
    book_cover = models.ImageField(upload_to='covers')

    def __str__(self):
        return f'{self.book_title}, from {self.book_authors}'
