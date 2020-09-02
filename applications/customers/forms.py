from django import forms

from .models import Customer, Landing

#create add/update customer form
class AddCustomer(forms.ModelForm):
    
    class Meta:
        model = Customer
        #here fields go in a tuple and not in a list
        fields = ('customer_name', 'customer_surname', 'customer_address')
        #adding form features with the widgets class variable
        widgets = {
            'customer_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the customer\'s name',
                    'class':'form-control'
                }
            ),
            'customer_surname': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the customer\'s surname',
                    'class':'form-control'
                }
            ),
            'customer_address': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the customer\'s address',
                    'class':'form-control'
                }
            ),           
        }


#add new landing form
class AddLanding(forms.ModelForm):
    
    class Meta:
        model = Landing
        #here fields go in a tuple and not in a list
        fields = ('customer', 'book', 'date_borrowed', 'date_due')
        #adding form features with the widgets class variable
        widgets = {
            'customer': forms.Select(
                attrs = {
                    'placeholder':'Select the customer',
                    'class':'form-control'
                }
            ),
            'book': forms.Select(
                attrs = {
                    'placeholder':'Select the book',
                    'class':'form-control'
                }
            ),
            'date_borrowed': forms.DateInput(
                attrs = {
                    'class':'form-control'
                }
            ),  
            'date_due': forms.DateInput(
                attrs = {
                    'class':'form-control'
                }
            ),         
        }


class ReturnedLanding(forms.ModelForm):

    class Meta:
        model = Landing
        fields = ('returned',)

        returned = forms.BooleanField(required=True)