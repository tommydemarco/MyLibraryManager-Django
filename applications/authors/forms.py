from django import forms

from .models import Author

#create employee form
class AddAuthor(forms.ModelForm):
    
    class Meta:
        model = Author
        #here fields go in a tuple and not in a list
        fields = ('author_name', 'author_surname', 'author_nationality', 'author_description')
        #adding form features with the widgets class variable
        widgets = {
            'author_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the title of the book',
                    'class':'form-control'
                }
            ),
            'author_surname': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),
            'author_nationality': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the phone number',
                    'class':'form-control'
                }
            ),
            'author_description': forms.TextInput(
                attrs = {
                    
                    'class':'form-control'
                }
            ),
            
        }