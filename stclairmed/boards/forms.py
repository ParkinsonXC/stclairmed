from django import forms
from .models import Specialty, Practice

class PracticeSearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=35,
        help_text = "The max length of the name is 35 letters."        
        )

    address = forms.CharField(
        max_length=50,
        help_text="The max length of the address is 50 letters."
        )

    class Meta:
        model = Practice
        fields = ['name', 'address']

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=35,
    )

    phone = forms.IntegerField()

    email = forms.EmailField()
    #TODO: Confirm your email field?
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':"Type your comment/question here."}
        ),
        max_length=4000,
        help_text="You may not type a message longer than 4000 characters."
    )

    class Meta:
        model = Specialty #TODO Add a new model that allows users to contact Elaine
        fields = ['name', 'phone', 'email', 'message']