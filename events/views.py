from django.shortcuts import render

# Create your views here.
# events/views.py
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Event

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        # Return only events that are in the future
        return Event.objects.filter(start_time__gte=timezone.now())

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/event_detail.html'