from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse
from .models import Subscriber, UnsubscribedEmail
from .thread import EmailThreading
from newsletter.forms import Subscribetoletter, SendNewsLetter, EditPreference, UnsubscribedEmailReason

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        email_already_exists = Subscriber.objects.filter(email=email).exists()
        print(email_already_exists)
        if email_already_exists:
            messages.error(request, "This email is already subscribed to our newsletter")
            return redirect('home')
        
        subscribedemail = Subscriber.objects.create(email=email, first_name= "", last_name="")
        request.session['subscribedemail'] = subscribedemail.slug
        messages.success(request, "Subscription confirmed")

        # html_template_path = "newsletter/new_subscriber_email.html"
        # context_data = {'first_name': first_name, 'edit_preference': domain_name + reverse('edit_preference', kwargs={'slug': obj.slug}), 'unsubscribe': domain_name + reverse("unsubscribe", kwargs={'slug': obj.slug}), 'privacy_link': domain_name + reverse('privacy')}
        # email_html_template = get_template(html_template_path).render(context_data)
        # receiver_email = email
        # email_msg = EmailMessage("Thanks for joining us", email_html_template, site_email, [receiver_email], reply_to=[site_email])
        # email_msg.content_subtype = 'html'
        # EmailThreading(email=email_msg).start()

        return redirect('subscription_confirmed')
    # else:
    #     for key, error in list(form.errors.items()):
    #         if key == 'captcha' and error[0] == 'This field is required.':
    #             messages.error(request, 'You must pass the reCAPTCHA ')
    #             continue
    #         messages.error(request, error)
    return render(request, 'newsletter/home.html', {
    })

def subscription_confirmed(request, *args, **kwargs):
    email_slug = request.session['subscribedemail']
    if email_slug:
        return render(request, 'newsletter/subscription_confirmed.html', {
            'email_slug': email_slug,
        })
    else:
        redirect('home')

def start_unsubscribe(request):
    if request.method =="POST":
        email = request.POST.get('email')
        # try:
        #     subscriber = Subscriber.objects.get(email=email)
        #     template_name = 'newsletter/unsubscribe_email.html'
        #     context = {'link': domain_name + reverse('unsubscribe', kwargs={'slug': subscriber.slug}), 'contact_link': domain_name + reverse('contact')}
        #     email_html_template = get_template(template_name).render(context)
        #     mail = EmailMessage(subject='Unsubscribe from our email', body=email_html_template, from_email=site_email, to = [subscriber.email])
        #     mail.content_subtype = 'html'
        #     mail.attach_alternative = (email_html_template, "text/html")
        #     EmailThreading(mail).start()
        #     messages.success(request, "unsubscribe Link has been sent to {}. Can't find the link? check your spam folder".format(email))
        #     return redirect('start_unsubscribe')
        # except Subscriber.DoesNotExist:
        #     messages.error(request, 'This email does not exist on our list')
        #     return render(request, 'newsletter/start_unsubscribe.html', {
        #     'written_email': email,
        # })
    return render(request, 'newsletter/start_unsubscribe.html', {

    })


def unsubscribe(request, slug):
    subscriber = get_object_or_404(Subscriber, slug=slug)
 
  

    if request.method == "POST":
        request.session['unsubscribed_email'] = subscriber.email
        subscriber.delete()
        messages.success(request, "Unsubscribed")
        return redirect('unsubscribe_successful')
    return render(request, 'newsletter/unsubscribe.html', {

    })

    

def unsubscribe_successful(request):
    if request.session.get('unsubscribed_email'):

        form = UnsubscribedEmailReason()
        if request.method == 'POST':
            form = UnsubscribedEmailReason(request.POST or None)
            if form.is_valid():
                if UnsubscribedEmail.objects.filter(email=request.session.get('unsubscribed_email')).exists():
                    messages.success(request, 'Thanks for the feedback')
                    return redirect('unsubscribe_successful')
                unsubscribedemail = form.save(commit=False)
                unsubscribedemail.email = request.session.get('unsubscribed_email')
                unsubscribedemail.save()
                messages.success(request, 'Thanks for the feedback')
                return redirect('unsubscribe_successful')
        return render(request, 'newsletter/unsubscribe_successful.html', {
            'form': form,
        })
    else:
        return redirect('unsubscribe')
    

def send_preference_link(request):
    return render(request,  'newsletter/send_preference_link.html', {

    })


def edit_preference(request, slug):
    preference = get_object_or_404(Subscriber, slug=slug)
    
    form = EditPreference(instance=preference)
    if request.method == 'POST':
        form = EditPreference(request.POST or None, instance=preference)
        if form.is_valid():
            form.save()
            messages.success(request, 'Preference update successful')
            return redirect('subscription_confirmed')
    return render(request, 'newsletter/edit_preference.html', {
        'form': form,
    })


@staff_member_required
def send_news_letter(request):
    form = SendNewsLetter()
    if request.method == "POST":
        form = SendNewsLetter(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Mass email letter sent successfully")
            return redirect('send_news_letter')
    return render(request, 'newsletter/send_news_letter.html', {
        'form': form,
    })
