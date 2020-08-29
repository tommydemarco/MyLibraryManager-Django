from django.db import models

#import the author manager 
from .managers import AuthorManager

#author models 

class Author(models.Model):
    """model for the authors"""

    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)
    author_nationality = models.CharField(max_length=50)
    author_age =  models.PositiveIntegerField()
    author_description = models.CharField(max_length=400)

    #delegating the request to the database to the manager
    objects = AuthorManager()

    def __str__(self):
        return f'{self.author_surname}, {self.author_name}'