from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from .models import Event, Host
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

        context['index_event_list'] = self._get_list(list_type)
        context['list_type'] = list_type
        return render(request, 'events/index.html', context)


class EventView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'