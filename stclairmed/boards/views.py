from django.shortcuts import render, redirect, get_object_or_404
from .models import Specialty, Practice, Doctor
from .forms import PracticeSearchForm, ContactForm

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
    practice_form = PracticeSearchForm()
    
    return render(request, 'directory.html', {'specialties':specialties, 'form': practice_form})

def contact(request):
    #TODO: Handle post requests
    contact_form = ContactForm()

    return render(request, 'contact.html', {'form':contact_form})

def officers(request):
    return render(request, 'officers.html')

def events(request):
    return render(request, 'events.html')

def news(request):
    return render(request, 'news.html')

def hospitals(request):
    return render(request, 'hospitals.html')

def links(request):
    return render(request, 'links.html')

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})

def newsletter(request):
    
    newsletters = reversed(Newsletter.objects.all())

    return render(request, 'newsletter.html', {'newsletters' : newsletters})