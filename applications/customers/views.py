from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView

from .models import Customer, Landing

from django.contrib import messages

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddCustomer, AddLanding, ReturnedLanding


class ListCustomers(LoginRequiredMixin, ListView):
    template_name = 'customers/list.html'
    model = Customer
    context_object_name = 'customers'
    paginate_by = 3

    def get_queryset(self):

        #for an author search, getting the name from the form
        name = self.request.GET.get("name", "")
        surname = self.request.GET.get("surname", "")

        if name:
            return Customer.objects.search_customer_by_name(name)
        elif surname:
            return Customer.objects.search_customer_by_surname(surname)
        else:
            #using the function of the manager to return the QuerySet
            return Customer.objects.list_customers()


class AddNewCustomer(LoginRequiredMixin, CreateView):
    template_name = 'customers/create.html'
    module = Customer
    
    form_class = AddCustomer

    #adding the url for when the process is complete.
    #required in a CreateView
    #syntax: 'urls_app_name:url_name'
    success_url = reverse_lazy('customers:customers')

    #THE FORM VALID  TAKES PLACE AFTER THE FORM HAS BEEN VALIDATED
    #adding attributes automatically using the method form_valid
    def form_valid(self, form):

        success_message = messages.add_message(self.request, messages.SUCCESS, 
        'The new customer has been successfully added to the database. You can now add a new landing for the customer')
        #syntax for returning the result  of the form valid
        return super(AddNewCustomer, self).form_valid(form)


class ListActiveLandings(LoginRequiredMixin, ListView):
    template_name = 'customers/list-landings.html'
    model = Landing
    context_object_name = 'active_landings'
    paginate_by = 1

    def get_queryset(self):

        book_name = self.request.GET.get("book", "")

        if book_name:
            return Landing.objects.list_active_landings_by_book(book_name)

        return Landing.objects.list_active_landings()

class ListReturnedLandings(LoginRequiredMixin, ListView):
    template_name = 'customers/list-returned-landings.html'
    model = Landing
    context_object_name = 'returned_landings'
    paginate_by = 1

    def get_queryset(self):
        return Landing.objects.list_returned_landings()


#add new landing
class AddNewLandingView(LoginRequiredMixin, CreateView):
    template_name = 'customers/add-new-landing.html'
    model = Landing 

    form_class = AddLanding

    success_url = reverse_lazy('customers:active_landings')

    #THE FORM VALID  TAKES PLACE AFTER THE FORM HAS BEEN VALIDATED
    #adding attributes automatically using the method form_valid
    def form_valid(self, form):

        success_message = messages.add_message(self.request, messages.SUCCESS, 
        'The new landing has been successfully added to the database. You have been redirected to the active \
            landings page.')
        #syntax for returning the result  of the form valid
        return super(AddNewLandingView, self).form_valid(form)


#checking a landing as returned
class ReturnedLanding(LoginRequiredMixin, UpdateView):
    template_name = 'customers/returned-landing.html'
    model = Landing 

    form_class = ReturnedLanding

    success_url = reverse_lazy('customers:active_landings')

    def form_valid(self, form):

        success_message = messages.add_message(self.request, messages.SUCCESS, 
        'The landing has been successfully marked as returned. You have been redirected to the active landings list.')
        return super(ReturnedLanding, self).form_valid(form)