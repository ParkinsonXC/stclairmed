from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Specialty, Practice, Doctor

from .forms import SearchForm, ContactForm
from .contact_email_confirm import contact_email
from events.models import Event, RSVP
from events.forms import RsvpForm, EventForm
from newsletters.models import Newsletter
from officers.models import Officer, Role
from news.models import Announcement

from events.event_rsvp_confirm_template import email_confirmation_html
from django.db.models import Q
from .tables import PracticeTable, SpecialtyTable, DoctorTable
import datetime



# Create your views here.
def home(request):
    contact_form = ContactForm()   
    if request.method == 'POST':
        #print('Is POST Request')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            send_mail(
                'SCCMS CONTACT - {0}'.format(name),
                '',
                from_email='neondodongo@gmail.com',
                # Change this to SCCMS email
                recipient_list=['neondodongo@gmail.com'],
                fail_silently=False,
                html_message=contact_email.format(name, email, message)
            )
            return render(request, 'contact_confirm.html')  
 
    return render(request, 'home.html', {'form':contact_form})
>>>>>>> gwi-6

def directory(request):
    #TODO: Handle post requests
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_field = form.cleaned_data.get('my_choice_field')
            # search_field = request.POST.get('my_choice_field')
            # query = request.POST.get('term')

            query = form.cleaned_data.get('term')

            #Creates the SQL needeed to search all selected practice fields
            practice_or_lookup = (Q(name__icontains=query) |
                             Q(address__icontains=query) |
                             Q(city__icontains=query) |
                             Q(state__icontains=query) |
                             Q(zip_code__icontains=query) |
                             Q(phone_number__icontains=query)|
                             Q(website__icontains=query)
                             )

            #Creates the SQL needed to search all selected doctor fields
            doctor_or_lookup = (Q(first_name__icontains=query) |
                             Q(last_name__icontains=query) |
                             Q(title__icontains=query)
                             )

            if search_field == 'practices':

                qs = Practice.objects.filter(practice_or_lookup).distinct()
                practice_table = PracticeTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'practice_table':practice_table})
                
            elif search_field == 'doctors':
                
                qs = Doctor.objects.filter(doctor_or_lookup).distinct()
                doctor_table = DoctorTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'doctor_table':doctor_table})

            else:
                practice_qs = Practice.objects.filter(practice_or_lookup).distinct()
                doctor_qs = Doctor.objects.filter(doctor_or_lookup).distinct()
                
                practice_table = PracticeTable(practice_qs)
                doctor_table = DoctorTable(doctor_qs)

                qs = []
                for i in practice_qs:
                    qs.append(' ')
                for i in doctor_qs:
                    qs.append(' ')            
            
                return render(request, 'directory_results.html', {'qs':qs, 'practice_table':practice_table, 'doctor_table':doctor_table})
                
                
    #if request.method == 'GET':
    specialties = Specialty.objects.order_by('name')
    form = SearchForm()
    
    return render(request, 'directory.html', {'specialties':specialties, 'form': form})

def officers(request):

    officers = Officer.objects.all()
    roles = Role.objects.all()

    return render(request, 'officers.html', {'officers':officers, 'roles':roles})

def events(request):
    events = reversed(Event.objects.all()) # Show newest event first
    form = RsvpForm()
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    return render(request, 'events.html', {'events':events, 'current_date':current_date, 'current_time':current_time})


def event_rsvp(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            event = get_object_or_404(Event, pk=pk)
            event.attendees = event.attendees + form.cleaned_data.get('guests') + 1
            event.save()
            rsvp = RSVP.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                event=event
            )
            send_mail(
                'Event Confirmation - SCCMS',
                '',
                from_email='neondodongo@gmail.com',
                recipient_list=[rsvp.email],
                fail_silently=False,
                html_message=email_confirmation_html.format(
                    event.title, 
                    event.location.name, 
                    event.location.address, 
                    event.location.city, 
                    event.location.state, 
                    '{0} {1}'.format(rsvp.first_name, rsvp.last_name),
                    event.description
                )
            )
            rsvp.save()
            return render(request, 'rsvp_confirm.html', {'rsvp':rsvp, 'event':event})
    else:
        form = RsvpForm()
    return render(request, 'event_rsvp.html', {'event':event, 'form':form})






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


def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})

def newsletter(request):
    
    newsletters = reversed(Newsletter.objects.all())

    return render(request, 'newsletter.html', {'newsletters' : newsletters})