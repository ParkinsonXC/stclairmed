from django import forms

from .models import Event, RSVP

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Event
        fields = ['description']

class RsvpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    guests = forms.IntegerField()

    class Meta:
        model = RSVP
        fields = [
            'first_name',
            'last_name',
            'email',
            'guests'
        ]
