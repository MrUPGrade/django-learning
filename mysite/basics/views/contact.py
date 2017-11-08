from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import basics.models as models
import basics.forms as forms


class ContactDetailView(DetailView, LoginRequiredMixin):
    template_name = 'basics/contact/details.html'
    model = models.Contact

    def get_queryset(self):
        return models.Contact.objects.all().prefetch_related('tags')


class AddContactView(View, LoginRequiredMixin):
    template = 'basics/contact/add.html'

    def get(self, request):
        form = forms.ContactForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('basics:contact-all'))

        return render(request, self.template, {'form': form})

@login_required
def all_contacts(request):
    contacts = list(models.Contact.objects.all())
    return render(request, 'basics/contact/all.html', {'contacts': contacts})
