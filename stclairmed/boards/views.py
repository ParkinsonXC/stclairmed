from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm
from events.models import Event, RSVP
from events.forms import RsvpForm, EventForm
from newsletters.models import Newsletter
from officers.models import Officer, Role
from news.models import Announcement
from django.db.models import Q
from .tables import PracticeTable, SpecialtyTable, DoctorTable



# Create your views here.
def home(request):
    #TODO: handle post requests
    contact_form = ContactForm()
    return render(request, 'home.html', {'form':contact_form})

def directory(request):
    #TODO: Handle post requests
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_field = form.cleaned_data.get('my_choice_field')
            # search_field = request.POST.get('my_choice_field')
            # query = request.POST.get('term')

            query = form.cleaned_data.get('term')
            if search_field == 'practices':
                or_lookup = (Q(name__icontains=query) |
                             Q(address__icontains=query) |
                             Q(city__icontains=query) |
                             Q(state__icontains=query) |
                             Q(zip_code__icontains=query) |
                             Q(phone_number__icontains=query)|
                             Q(website__icontains=query)
                             )
                
                qs = Practice.objects.filter(or_lookup).distinct()
                table_qs = PracticeTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'table_qs':table_qs})

            elif search_field =='specialty':
                or_lookup = (Q(name__icontains=query) |
                             Q(description__icontains=query)
                             )
                qs = Specialty.objects.filter(or_lookup).distinct()
                table_qs = SpecialtyTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'table_qs': table_qs})
                

            elif search_field == 'doctors':
                or_lookup = (Q(first_name__icontains=query) |
                             Q(last_name__icontains=query) |
                             Q(title__icontains=query)
                             )
                qs = Doctor.objects.filter(or_lookup).distinct()
                table_qs = DoctorTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'table_qs':table_qs})

            else:
                 pass
                
                
    #if request.method == 'GET':
    specialties = Specialty.objects.order_by('name')
    form = SearchForm()
    
    return render(request, 'directory.html', {'specialties':specialties, 'form': form})

def contact(request):
    #TODO: Handle post requests
    contact_form = ContactForm()

    return render(request, 'contact.html', {'form':contact_form})

def officers(request):

    officers = Officer.objects.all()
    roles = Role.objects.all()

    return render(request, 'officers.html', {'officers':officers, 'roles':roles})

def events(request):
    events = reversed(Event.objects.all()) # Show newest event first
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            pk = request.POST['event-id']
            event = get_object_or_404(Event, pk=pk)
            event.attendees = event.attendees + form.cleaned_data.get('guests') + 1
            event.save()
            rsvp = RSVP.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                guests=form.cleaned_data.get('guests'),
                event=event
            )
            # TODO: Send verification email to user
            # TODO: Increment event 'attendees' field for each rsvp + guests
            return render(request, 'rsvp_confirm.html', {'rsvp':rsvp, 'event':event})
    else:
        form = RsvpForm()
    return render(request, 'events.html', {'events':events, 'form':form})






def news(request):
    announcements_list = Announcement.objects.all().order_by('-date', '-time')
    page = request.GET.get('page', 1)

    paginator = Paginator(announcements_list, 3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'announcements' : announcements})






def hospitals(request):
    return render(request, 'hospitals.html')

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})

def newsletter(request):
    
    newsletters = reversed(Newsletter.objects.all())

    return render(request, 'newsletter.html', {'newsletters' : newsletters})