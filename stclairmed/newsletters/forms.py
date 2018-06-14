from django import forms
from .models import Newsletter, Subscriber

class SubForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        min_length=3,
        max_length=30
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}),
        min_length=3,
        max_length=50
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder' : 'E-Mail'}),
        max_length=100
    )

    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email']

class UnsubForm(forms.Form):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder' : 'E-Mail'}),
        max_length=100,
        min_length=1,
    )

    class Meta:
        fields = ['email']