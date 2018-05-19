from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Event
        fields = ['description']
