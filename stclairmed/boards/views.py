from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm
from events.models import Event, RSVP
from events.forms import RsvpForm, EventForm
from newsletters.forms import SubForm
from newsletters.models import Newsletter, Subscriber
from officers.models import Officer, Role
from news.models import Announcement

from events.event_rsvp_confirm_template import email_confirmation_html
from newsletters.newsletter_sub_confirm import sub_confirmation_html
from django.db.models import Q
from .tables import PracticeTable, SpecialtyTable, DoctorTable
import datetime



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

            #Creates the SQL needed to search all selected specialty fields TODO: Is this necessary?
            specialty_or_lookup = (Q(name__icontains=query) |
                             Q(description__icontains=query)
                             )

            if search_field == 'practices':

                qs = Practice.objects.filter(practice_or_lookup).distinct()
                table_qs = PracticeTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'table_qs':table_qs})

            elif search_field =='specialty':
                
                qs = Specialty.objects.filter(specialty_or_lookup).distinct()
                table_qs = SpecialtyTable(qs)
                return render(request, 'directory_results.html', {'qs':qs, 'table_qs': table_qs})
                
            elif search_field == 'doctors':
                
                qs = Doctor.objects.filter(doctor_or_lookup).distinct()
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






def hospitals(request):
    return render(request, 'hospitals.html')

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})

def newsletter(request):
    
    reversed_newsletters = reversed(Newsletter.objects.all())
    newsletters = Newsletter.objects.all().order_by('-date')
    

    if request.method == 'POST':
        if 'subscribe_submit' in request.POST:
            newsletter = newsletters[0]
            form = SubForm(request.POST)
            if form.is_valid():
                sub = Subscriber.objects.create(
                    first_name=form.cleaned_data.get('first_name').lower(),
                    last_name=form.cleaned_data.get('last_name').lower(),
                    email=form.cleaned_data.get('email').lower()
                )
                send_mail(
                    'Subscription Confirmation - SCCMS',
                    '',
                    from_email='neondodongo@gmail.com',
                    recipient_list=[sub.email],
                    fail_silently=False,
                    html_message=sub_confirmation_html.format(
                        '{0} {1}'.format(sub.first_name, sub.last_name),
                        '{0} {1}'.format(newsletter.month, newsletter.year),
                        newsletter.pdf_file.url,
                        newsletter.pdf_img.url
                    )
                )
                sub.save()
                return render(request, 'sub_confirm.html', {'sub':sub, 'newsletter':newsletter})
        
        elif 'unsubscribe_submit' in request.POST:
            form = SubForm(request.POST)
            if form.is_valid():
                unsub_first = form.cleaned_data.get('first_name').lower()
                unsub_last = form.cleaned_data.get('last_name').lower()
                unsub_email = form.cleaned_data.get('email').lower()

                sub = Subscriber.object.all().filter(email = unsub_email).distinct()
                send_mail(
                    'Unsubscription Confirmation - SCCMS',
                    '',
                    from_email='neondodongo@gmail.com',
                    recipient_list=[sub.email],
                    fail_silently=False,
                    html_message=unsub_confirmation_html.format(
                        '{0} {1}'.format(sub.first_name, sub.last_name),
                    )
                )
                sub.delete()
                return render(request, 'unsub_confirm.html', {'sub':sub})
        else:
            form = SubForm()

    return render(request, 'newsletter.html', {'newsletters' : reversed_newsletters, "form" : form})