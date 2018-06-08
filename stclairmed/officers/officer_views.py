from django.shortcuts import render
from .models import Officer, Role

def officers(request):

    officers = Officer.objects.all()
    roles = Role.objects.all()

    return render(request, 'officers.html', {'officers':officers, 'roles':roles})