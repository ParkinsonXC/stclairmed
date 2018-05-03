from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialty

# Create your views here.
def home(request):
    return render(request, 'home.html')

def directory(request):
    specialties = Specialty.objects.all()
    spec_names = list()
    
    for field in specialties:
        spec_names.append(field.name)

    response_html = '<br>'.join(spec_names)

    return render(request, 'directory.html')

def about(request):
    return render(request, 'about.html')

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