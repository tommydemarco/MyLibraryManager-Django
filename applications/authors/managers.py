from django.db import models 

#import the function that allows you to make "or" statements in the database consult
from django.db.models import Q

class AuthorManager(models.Manager):
    """Manager for the Author model"""

    #general list including all objects
    def list_authors(self):
        return self.all()

    #search by name function
    def search_author_by_name(self, keyword):
        #using icontains to get the similar results 
        #(actually looking for the surname as well with the or and the Q functions)
        search_result_name = self.filter(
            Q(author_name__icontains=keyword) or Q(author_surname__icontains=keyword)
            )
        return search_result_name

    #search by surname function
    def search_author_by_surname(self, keyword):
        search_result_surname = self.filter(author_surname__icontains=keyword)
        return search_result_surname