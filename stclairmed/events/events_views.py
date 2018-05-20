from django.shortcuts import render

from events.models import Event
from events.forms import RsvpForm

def event_rsvp(request, pk):
    event = get_object_or_404(Events, pk=pk)
    form = RsvpForm()
    return render(request, 'rsvp.html', {'event':event, 'form':form})