from django.shortcuts import render, redirect, get_object_or_404
from .models import Specialty, Practice

# Create your views here.
def home(request):
    return render(request, 'home.html')

def directory(request):
    specialties = Specialty.objects.all()
    return render(request, 'directory.html', {'specialties':specialties})

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

def contact(request):
    return render(request, 'contact.html')

def spec_description(request, pk):
    spec = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html')