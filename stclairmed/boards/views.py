from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail.message import EmailMessage
from django.db.models import Q

from .models import Specialty, Practice, Doctor
from .forms import SearchForm, ContactForm
from .contact_email_confirm import contact_email
from .tables import PracticeTable, SpecialtyTable, DoctorTable

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

def spec_description(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)

    return render(request, 'spec_description.html', {'specialty': specialty})




