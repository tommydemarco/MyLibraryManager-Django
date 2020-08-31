import datetime

from django.db import models 

#import the function that allows you to make "or" statements in the database consult
from django.db.models import Q

class BookManager(models.Manager):
    """Manager for the Book model"""

    #search by date published function
    def search_books_by_date_published(self, keyword1, keyword2):

        keyword1 = datetime.datetime.strptime(keyword1, '%Y-%m-%d').date()
        keyword2 = datetime.datetime.strptime(keyword2, '%Y-%m-%d').date()

        #formatting the dates

        search_result_date = self.filter(
            date_published__range=(keyword1, keyword2)
            )

        return search_result_date

    #searche by genere
    def search_books_by_genere(self, id):

        search_result_genere = self.filter(
            book_category__id = id
        ).order_by('book_title')

        return search_result_genere