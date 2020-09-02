from django.db import models

#importing the book module 
from applications.books.models import Book

#importing the manager
from .managers import CustomerManager, LandingManager

#customer module
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_surname = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=40)

    objects = CustomerManager()

    def __str__(self):
        return f'{self.customer_surname}, {self.customer_name}'

#landings model
class Landing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_landing")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_landing")
    date_borrowed = models.DateField()
    date_due = models.DateField()
    #could be the source of errors
    returned = models.BooleanField(default=False,)

    book_returned = "No"
    if returned:
        book_returned = "Yes"

    objects = LandingManager()


    def __str__(self):
        return f'{self.book} was landed to: {self.customer}, due on: {self.date_due}. \
                Returned? {self.book_returned}'




