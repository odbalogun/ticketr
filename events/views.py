from django.views.generic import CreateView
from django.shortcuts import render


class EventCreateView(CreateView):
    template_name = 'events/create.html'


