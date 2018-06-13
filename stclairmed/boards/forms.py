from django import forms
from .models import Specialty, Practice

class SearchForm(forms.Form):
    term = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search term...',            
            }
        ),
        required = True,
        max_length = 35,
        help_text = "The max length of the term is 35 letters."        
        )

    choices = (('practices', 'Practices',),('doctors', 'Doctors',),('all', 'All',))
    my_choice_field = forms.ChoiceField(
        widget=forms.RadioSelect(), 
        required=True,
        choices=choices,
        help_text="Select a field to search in, or select 'All' to search all fields")
    

    class Meta:
        fields = ['term', 'field']

class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=35,
    )

    email = forms.EmailField(
        required=True,
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':"Type your comment/question here."}
        ),
        required=True,
        max_length=4000,
        help_text="You may not type a message longer than 4000 characters."
    )

    class Meta:
        fields = ['name', 'email', 'message']


class SuperSearch(forms.Form):
    keyword = forms.CharField(
        max_length = 45,
        min_length = 1
    )

    class Meta:
        fields = ['keyword']
