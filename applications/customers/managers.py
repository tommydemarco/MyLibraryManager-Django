from django.db import models 

#import the function that allows you to make "or" statements in the database consult
from django.db.models import Q

class CustomerManager(models.Manager):
    """Manager for the Author model"""

    #general list including all objects
    def list_customers(self):
        return self.all()

    #search by name function
    def search_customer_by_name(self, keyword):
        #using icontains to get the similar results 

        #(actually looking for the surname as well with the or and the Q functions)
        # search_result_name = self.filter(
        #     Q(author_name__icontains=keyword) | Q(author_surname__icontains=keyword)
        #     )

        search_result_name = self.filter(
            customer_name__icontains=keyword
            ).order_by('customer_name')
            #.exclude(author_age<35)   //would exclude according to the filter

        return search_result_name

    #search by surname function
    def search_customer_by_surname(self, keyword):
        search_result_surname = self.filter(customer_surname__icontains=keyword).order_by('customer_name')
        return search_result_surname


class LandingManager(models.Manager):
    """Manager for the Landings model"""

    def list_active_landings(self):
        search_result_active = self.filter(
            returned=False
            ).order_by('book')

        return search_result_active

    def list_active_landings_by_book(self, keyword):

        search_result_by_book = self.filter(
                book=keyword, #returned=False,
            ).order_by('book')

        return search_result_by_book

    def list_returned_landings(self):
        search_result_returned = self.filter(
            returned=True
            ).order_by('book')

        return search_result_returned
