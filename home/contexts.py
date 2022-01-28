from django.contrib import messages

from .forms import NewsletterForm
from .models import Subscribers
from django.core.mail import send_mail
from django.conf import settings


def newsletter(request):
    """
    A view to allow the user to subscribe to the newsletter
    """
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if Subscribers.objects.filter(
                    email=instance.email).exists():
                messages.error(request,
                               'Sorry, that email already exists in our list')
            else:
                instance.save()
                messages.success(request,
                                 'Thank you for subscribing \
                                 to our newsletter')
                sender_email = instance.email
                send_mail(
                    'Thank you for subscribing to this newsletter!',
                    'I hope you enjoyed browsing the products on our store.',
                    settings.DEFAULT_FROM_EMAIL,
                    [sender_email],
                )
    else:
        newsletter_form = NewsletterForm()

    context = {
        'newsletter_form': newsletter_form,
        }

    return context
