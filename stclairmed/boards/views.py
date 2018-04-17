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
    response_html = '<h1>About Us Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def officers(request):
    response_html = '<h1>Officers Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def events(request):
    response_html = '<h1>Events Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def news(request):
    response_html = '<h1>News Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def hospitals(request):
    response_html = '<h1>Hospitals Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def links(request):
    response_html = '<h1>Links Page</h1>'
    return HttpResponse(response_html) #TODO: Create template

def contact(request):
    response_html = '<h1>Contact Page</h1>'
    return HttpResponse(response_html) #TODO: Create template