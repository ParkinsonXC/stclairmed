from django import forms
from .models import Event, RSVP

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Event
        fields = ['description']

class RsvpForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        min_length=3,
        max_length=20
    )
    last_name = forms.CharField(max_length=40, 
        widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'E-Mail'})
    )
    guests = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Guests'}),
        min_value=0,
        max_value=20
        )

    class Meta:
        model = RSVP
        fields = [
            'first_name',
            'last_name',
            'email',
            'guests'
        ]
