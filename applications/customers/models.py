from django.db import models

#importing the book module 
from applications.books.models import Book

#customer module
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_surname = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=40)

    def __str__(self):
        return f'Customer full name: {self.customer_surname}, from {self.customer_name}'

#landings model
class Landing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    date_due = models.DateField()
    returned = models.BooleanField()

    book_returned = "No"

    if returned:
        book_returned = "Yes"


    def __str__(self):
        return f'{self.book} was landed to: {self.customer}, due on: {self.date_due}. \
                Returned? {self.book_returned}'




