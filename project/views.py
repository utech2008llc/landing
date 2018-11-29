from django.shortcuts import render
from django.http import HttpResponseRedirect

from clients.forms import ContactForm
from subscribers.forms import SubscriberForm


def home_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    form_subscribers = SubscriberForm(request.POST or None)
    if form_subscribers.is_valid():
        form_subscribers.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'form_subscribers': form_subscribers
    }
    return render(request, "index.html", context)