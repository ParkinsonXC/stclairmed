from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm
from events.models import Event, RSVP
from events.forms import RsvpForm, EventForm
from newsletters.models import Newsletter
from officers.models import Officer, Role
from news.models import Announcement




# Create your views here.
def home(request):
    #TODO: handle post requests
    contact_form = ContactForm()
    return render(request, 'home.html', {'form':contact_form})

def directory(request):
    #TODO: Handle post requests
    
    specialties = Specialty.objects.order_by('name')
    form = SearchForm()
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         search_field = request.POST.get("my_choice_field")
    #         if search_field == 'practices':
    #             pass #TODO
    #         elif search_field =='specialty':
    #             pass #TODO
    #         elif search_field == 'doctors':
    #             pass #TODO
    #         else:
    #             #search_field == 'all' #TODO
        

    
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