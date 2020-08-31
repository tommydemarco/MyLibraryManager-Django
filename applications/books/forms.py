from django import forms

#importing the model
from .models import Book


#create employee form
class AddBook(forms.ModelForm):
    
    class Meta:
        model = Book
        #here fields go in a tuple and not in a list
        fields = ('book_title', 'book_category', 'book_authors', 'date_published', 'book_description')
        #adding form features with the widgets class variable
        widgets = {
            'book_title': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the title of the book',
                    'class':'form-control'
                }
            ),
            'book_authors': forms.Select(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),
            'date_published': forms.DateInput(
                attrs = {
                    'placeholder':'Insert the phone number',
                    'class':'form-control'
                }
            ),
            'book_category': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'book_description': forms.TextInput(
                attrs = {
                    'class':'form-control'
                },
            ),
            
        }

    #very powerful custom validation process
    #syntax: clean_field_name, can only validate one value at the time
    def clean_first_name(self):
        #getting the value first_name from the cleaned data
        first_name = self.cleaned_data['first_name']
        if first_name == "Default":
            raise forms.ValidationError("The default value is not accepted as a name")

        return first_name
