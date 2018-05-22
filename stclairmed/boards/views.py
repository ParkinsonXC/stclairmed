from django.shortcuts import render, redirect, get_object_or_404
from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm

# The import below has been added for newsletter functionality
from newsletters.models import Newsletter




# Create your views here.
def home(request):
    #TODO: handle post requests
    contact_form = ContactForm()
    return render(request, 'home.html', {'form':contact_form})

def directory(request):
    #TODO: Handle post requests
    
    specialties = Specialty.objects.all()
    search_form = SearchForm()

    return render(request, 'directory.html', {'specialties':specialties, 'form':search_form})

def contact(request):
    #TODO: Handle post requests
    contact_form = ContactForm()

    return render(request, 'contact.html', {'form':contact_form})

def officers(request):
    return render(request, 'officers.html')

def events(request):
    events = reversed(Event.objects.all()) # Show newest event first
    if request.method == 'POST':
        pk = request.POST['event-id']
        event = get_object_or_404(Event, pk=pk)
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp = RSVP.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                guests=form.cleaned_data.get('guests'),
                event=event
            )
            # TODO: Send verification email to user
            # TODO: Increment event 'attendees' field for each rsvp + guests
            return render(request, 'rsvp_confirm.html', {'email':rsvp.email})
    else:
        form = RsvpForm()
    return render(request, 'events.html', {'events':events, 'form':form})

def news(request):
    return render(request, 'news.html')

def hospitals(request):
    return render(request, 'hospitals.html')

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})

def newsletter(request):
    
    newsletters = reversed(Newsletter.objects.all())

    return render(request, 'newsletter.html', {'newsletters' : newsletters})