from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm, SuperSearch
from .contact_email_confirm import contact_email
from .tables import PracticeTable, SpecialtyTable, DoctorTable
from .functions import practice_or_lookup, doctor_or_lookup, event_or_lookup, announcement_or_lookup, newsletter_or_lookup

from events.models import Event
from events.tables import EventTable
from news.models import Announcement
from news.tables import AnnouncementTable
from newsletters.models import Newsletter
from newsletters.tables import NewsletterTable
from officers.models import Officer, Role
from officers.tables import OfficerTable

# Create your views here.
def home(request):
    contact_form = ContactForm()
    supersearch_form = SuperSearch()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        supersearch_form = SuperSearch(request.POST)

        if 'contact' in request.POST:
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
            
        else:
            if supersearch_form.is_valid():
                query = supersearch_form.cleaned_data.get('keyword')

                practices_sql = practice_or_lookup(query)
                doctors_sql = doctor_or_lookup(query)
                event_sql = event_or_lookup(query)
                announcement_sql = announcement_or_lookup(query)
                newsletter_sql = newsletter_or_lookup(query)
                
                practice_set = Practice.objects.filter(practices_sql).distinct()
                doctor_set = Doctor.objects.filter(doctors_sql).distinct()
                event_set = Event.objects.filter(event_sql).distinct()
                announcement_set = Announcement.objects.filter(announcement_sql).distinct()
                newsletter_set = Newsletter.objects.filter(newsletter_sql).distinct()

                qs = [practice_set, doctor_set, event_set, announcement_set, newsletter_set]
                results = 0
                
                for query_set in qs:
                    if len(query_set) == 0:
                        qs.remove(query_set)

                    for i in query_set:
                        results += 1


                practice_table = PracticeTable(practice_set)
                doctor_table = DoctorTable(doctor_set)
                event_table = EventTable(event_set)
                announcement_table = AnnouncementTable(announcement_set)
                newsletter_table = NewsletterTable(newsletter_set)


    
                return render(request, 'supersearch_results.html', {'results':results, 'practice_table':practice_table,
                                                                'doctor_table':doctor_table, 
                                                                'event_table':event_table,
                                                                'announcement_table':announcement_table,
                                                                'newsletter_table':newsletter_table})
            else:
                error = "No results for empty query."
                contact_form = ContactForm()
                supersearch_form = SuperSearch()
                return render(request, 'home.html', {'contact_form':contact_form, 'supersearch_form': supersearch_form, 'super_error':error})          
 
    president = Officer.objects.get(position="President")
    
    return render(request, 'home.html', {'contact_form':contact_form, 'supersearch_form':supersearch_form,
                                            'president':president})

def directory(request):
    #TODO: Handle post requests
    specialties = Specialty.objects.order_by('name')
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

                qs = Practice.objects.filter(practice_or_lookup(query)).distinct()
                practice_table = PracticeTable(qs)
                form = SearchForm()
                return render(request, 'directory_results.html', {'qs':qs, 'practice_table':practice_table, 'form':form})
                
            elif search_field == 'doctors':
                
                qs = Doctor.objects.filter(doctor_or_lookup(query)).distinct()
                doctor_table = DoctorTable(qs)
                form = SearchForm()
                return render(request, 'directory_results.html', {'qs':qs, 'doctor_table':doctor_table, 'form':form})

            else:
                practice_qs = Practice.objects.filter(practice_or_lookup(query)).distinct()
                doctor_qs = Doctor.objects.filter(doctor_or_lookup(query)).distinct()
                
                practice_table = PracticeTable(practice_qs)
                doctor_table = DoctorTable(doctor_qs)

                qs = []
                for i in practice_qs:
                    qs.append(' ')
                for i in doctor_qs:
                    qs.append(' ')            
            
                form = SearchForm()
                return render(request, 'directory_results.html', {'qs':qs, 'practice_table':practice_table, 'doctor_table':doctor_table, 'form':form})
        else:
            error = "No results for empty query."
            form = SearchForm()
            return render(request, 'directory.html', {'form':form, 'error':error, 'specialties': specialties})  


    #if request.method == 'GET':
    form = SearchForm()
    
    return render(request, 'directory.html', {'specialties':specialties, 'form': form})

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})




