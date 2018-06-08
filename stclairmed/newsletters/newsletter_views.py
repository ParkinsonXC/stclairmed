from django.shortcuts import render
from django.db.models.base import ObjectDoesNotExist
from django.core.mail.message import EmailMessage

from .models import Newsletter, Subscriber
from .forms import SubForm, UnsubForm
from .newsletter_sub_confirm import sub_confirmation_html, unsub_confirmation_html

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