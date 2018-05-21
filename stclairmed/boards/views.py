from django.shortcuts import render, redirect, get_object_or_404
from .models import Specialty, Practice, Doctor
from .forms import PracticeSearchForm, ContactForm
from events.forms import RsvpForm
from events.models import Event, RSVP

# Create your views here.
def home(request):
    #TODO: handle post requests
    contact_form = ContactForm()
    return render(request, 'home.html', {'form':contact_form})

def directory(request):
    #TODO: Handle post requests
    
    specialties = Specialty.objects.all()
    practice_form = PracticeSearchForm()
    
    return render(request, 'directory.html', {'specialties':specialties, 'form': practice_form})

def contact(request):
    #TODO: Handle post requests
    contact_form = ContactForm()

    return render(request, 'contact.html', {'form':contact_form})

def officers(request):
    return render(request, 'officers.html')

def events(request):
    events = reversed(Event.objects.all()) # Show newest event first
    form = RsvpForm()
    return render(request, 'events.html', {'events':events, 'form':form})

def event_rsvp(request, pk):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk)
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp = RSVP.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                guests=form.cleaned_data.get('guests'),
                event=event
            )
            return render(request, 'event_confirm.html', {'email':rsvp.email})

    return redirect('events')

def news(request):
    return render(request, 'news.html')

def hospitals(request):
    return render(request, 'hospitals.html')

def links(request):
    return render(request, 'links.html')

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})