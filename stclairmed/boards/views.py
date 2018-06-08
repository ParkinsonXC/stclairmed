from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from django.core.mail.message import EmailMessage
from django.db.models.base import ObjectDoesNotExist

from .models import Specialty, Practice, Doctor

from .forms import SearchForm, ContactForm, SuperSearch
from .contact_email_confirm import contact_email
from events.models import Event, RSVP
from events.forms import RsvpForm, EventForm
from newsletters.forms import SubForm, UnsubForm
from newsletters.models import Newsletter, Subscriber
from officers.models import Officer, Role
from news.models import Announcement

from events.event_rsvp_confirm_template import email_confirmation_html
from newsletters.newsletter_sub_confirm import sub_confirmation_html, unsub_confirmation_html
from django.db.models import Q
from .tables import PracticeTable, SpecialtyTable, DoctorTable
import datetime



# Create your views here.
def home(request):
    contact_form = ContactForm()
    supersearch_form = SuperSearch()

    if request.method == 'POST':
        #print('Is POST Request')
        contact_form = ContactForm(request.POST)
        supersearch_form = SuperSearch(request.POST)

        if contact_form.is_valid():
            print('Form is valid')
            name = contact_form.cleaned_data.get('name')
            phone = contact_form.cleaned_data.get('phone')
            email = contact_form.cleaned_data.get('email')
            message = contact_form.cleaned_data.get('message')

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
        
        elif supersearch_form.is_valid():
            pass 
            
 
    return render(request, 'home.html', {'form':contact_form, 'supersearch_form':supersearch_form})

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

            #Creates the SQL needed to search all selected doctor fields

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
                # send_mail(
                #     'Subscription Confirmation - SCCMS',
                #     '',
                #     from_email='neondodongo@gmail.com',
                #     recipient_list=[sub.email],
                #     fail_silently=False,
                #     html_message=sub_confirmation_html.format(
                #         '{0} {1}'.format(sub.first_name, sub.last_name),
                #         '{0} {1}'.format(newsletter.month, newsletter.year),
                #         newsletter.pdf_file.url,
                #         newsletter.pdf_img.url
                #     )
                # )
                email = EmailMessage()
                email.content_subtype = "html"
                email.subject = "Subscription Confirmation"
                email.body = sub_confirmation_html.format(
                        '{0} {1}'.format(sub.first_name, sub.last_name)
                    )
                # email.from_email = "St. Clair County Medical Society <spencer.tyminski@gmail.com>"
                email.to = [sub.email]
                email.attach(''+ newsletter.month + '' + newsletter.year + '.pdf', newsletter.pdf_file.read(), mimetype="application/pdf") # Attach a file directly

                email.send() 
                sub.save()
                return render(request, 'sub_confirm.html', {'sub':sub, 'newsletter':newsletter})
        
        else:
            form = SubForm()
    else:
        form = SubForm()

    return render(request, 'newsletter.html', {'newsletters' : reversed_newsletters, "form" : form})


def unsubscribe(request):

    if request.method == "POST":
        form = UnsubForm(request.POST)
        if form.is_valid():
            unsub_email = form.cleaned_data.get('email').lower()

            try:
                unsub = Subscriber.objects.get(email = unsub_email)
            except ObjectDoesNotExist:
                error = "Subscriber does not exist"
                form = UnsubForm()
                return render(request, 'unsubscribe.html', {"form" : form, "error" : error})

            send_mail(
                'Unsubscription Confirmation - SCCMS',
                '',
                from_email='spencer.tyminski@gmail.com',
                recipient_list=[unsub.email],
                fail_silently=False,
                html_message=unsub_confirmation_html.format(
                    '{0} {1}'.format(unsub.first_name, unsub.last_name),
                )
            )
            # unsub.delete()
            form = UnsubForm()
            sent_unsub_link_confirmation = "An E-Mail containing the unsubscription confirmation link has been sent to " + unsub.email
            return render(request, 'unsubscribe.html', {'form':form, 'unsubconf':sent_unsub_link_confirmation})
        else:
            form = SubForm()
            return render(request, 'newsletter.html', {"form" : form})
    else:
        form = UnsubForm()

    return render(request, 'unsubscribe.html', {"form" : form})

def unsub_confirmation(request):

    #TODO Create Token before sending the unsub confirmation link to the user
    #TODO Receieve Token, find subscriber, and subscriber.delete() then present the confirmation page

    return render(request, 'unsub_confirm.html')

