from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from basics.forms import TagsAddForm
from basics.models import Tag


class TagsView(View):
    def get(self, request):
        tags_counts = Tag.objects.values('name').annotate(count=Count('contacts__id'))
        return render(request, 'basics/tags/stats.html', {'tags_counts': tags_counts})


class AddTagsView(View):
    template_name = 'basics/tags/add.html'

    def render_form(self, request, form):
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = TagsAddForm()
        return self.render_form(request, form)

    def post(self, request):
        form = TagsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('basics:tags'))
        return self.render_form(request, form)
