from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from .event_rsvp_confirm_template import email_confirmation_html
from .models import Event, RSVP
from .forms import RsvpForm

import datetime

def events(request):
    events = reversed(Event.objects.all()) # Show newest event first
    form = RsvpForm()
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    return render(request, 'events.html', {'events':events, 'current_date':current_date, 'current_time':current_time})

def event_rsvp(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            event = get_object_or_404(Event, pk=pk)
            event.attendees = event.attendees + form.cleaned_data.get('guests') + 1
            event.save()
            rsvp = RSVP.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                event=event
            )
            send_mail(
                'Event Confirmation - SCCMS',
                '',
                from_email='neondodongo@gmail.com',
                recipient_list=[rsvp.email],
                fail_silently=False,
                html_message=email_confirmation_html.format(
                    event.title, 
                    event.location.name, 
                    event.location.address, 
                    event.location.city, 
                    event.location.state, 
                    '{0} {1}'.format(rsvp.first_name, rsvp.last_name),
                    event.description
                )
            )
            rsvp.save()
            return render(request, 'rsvp_confirm.html', {'rsvp':rsvp, 'event':event})
    else:
        form = RsvpForm()
    return render(request, 'event_rsvp.html', {'event':event, 'form':form})
