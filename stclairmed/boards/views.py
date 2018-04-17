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
