from django.db import models

#author models 

class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)
    author_nationality = models.CharField(max_length=50)
    author_age =  models.PositiveIntegerField()

    def __str__(self):
        return f'{self.author_surname}, {self.author_name}'