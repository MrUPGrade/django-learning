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
        return self.model.objects.prefetch_related('tags')


class AddContactView(View, LoginRequiredMixin):
    template = 'basics/contact/add.html'

    def get(self, request):
        form = forms.ContactForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contanct = form.save(commit=False)
            contanct.user = request.user
            contanct.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('basics:contact-all'))

        return render(request, self.template, {'form': form})

@login_required
def all_contacts(request):
    contacts = models.Contact.objects.filter(user=request.user)
    return render(request, 'basics/contact/all.html', {'contacts': contacts})
