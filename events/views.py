from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from .models import Event, Host, search_events
from .forms import EventForm, SearchForm
# Create your views here.

class IndexView(generic.View):
    max_on_page = 5

    def _get_popular_events(self):
        events = []
        for event in Event.objects.order_by('-likes'):
            if event.has_not_ended():
                events.append(event)
            if len(events) == self.max_on_page:
                return events
        return events

    def _get_upcoming_events(self):
        events = []
        for event in Event.objects.order_by('start_date'):
            if event.has_not_ended() and event.is_upcoming():
                events.append(event)
            if len(events) == self.max_on_page:
                return events
        return events

    def _get_list(self, list_type):
        if list_type == 'upcoming':
            return self._get_upcoming_events()
        elif list_type == 'popular':
            return self._get_popular_events()
            
    def get(self, request):
        context = {}
        list_type = 'popular'
        if 'upcoming' in request.GET:
            list_type = 'upcoming'

        context['event_list'] = self._get_list(list_type)
        context['list_type'] = list_type
        return render(request, 'events/index.html', context)


class EventView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


@login_required
def add_event(request):
    form = EventForm(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            category = form.cleaned_data['category']
            is_event = form.cleaned_data['is_event']

            new_event = Event(title=title, description=description, 
                start_date=start_date, end_date=end_date, host=request.user,
                category=category)

            new_event.save()
            messages.add_message(request, messages.SUCCESS, 'Eveniment adaugat cu success!')
            return redirect('events:detail', pk=new_event.id)
    else:
        form = EventForm()
    return render(request, 'events/add.html', {'form': form})


def search(request):
    form = SearchForm(request.GET, initial={'is_event': True})
    event_list = []
    if form.is_valid():
        keyword = form.cleaned_data['keyword']
        is_offer = form.cleaned_data['is_offer']
        from_date = form.cleaned_data['from_date']
        category = form.cleaned_data['category']
        sort_criteria = form.cleaned_data['sort_criteria']

        event_list = search_events(keyword=keyword, is_offer=is_offer, 
            from_date=from_date, category=category, sort_criteria=sort_criteria)
    return render(request, 'events/search.html', {'form': form, 'event_list': event_list})

@login_required
def logout(request):
    logout(request)
    # Redirect to a success page.


class SearchView(generic.ListView):
    template_name = 'events/search.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            pass
        else:
            return None
