from django.db import models 

#import the function that allows you to make "or" statements in the database consult
from django.db.models import Q

class BookManager(models.Manager):
    """Manager for the Book model"""

    #search by date published function
    def search_books_by_date_published(self, keyword1, keyword2):

        search_result_date = self.filter(
            date_published__range=(keyword1, keyword2)
            )

        return search_result_date