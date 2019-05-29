from django.views.generic import CreateView, DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Event
from .forms import EventFormModel, TicketFormSet


def create_event(request):
    event = Event(organizer=request.user, organizer_name=request.user.company)

    if request.POST:
        form = EventFormModel(request.POST, request.FILES, instance=event)
        ticket_set = TicketFormSet(request.POST, instance=event)

        if form.is_valid() and ticket_set.is_valid():
            form.save()
            ticket_set.save()
            # redirect
            return HttpResponseRedirect(reverse_lazy("events:detail", kwargs={'pk': event.pk}))
        else:
            if form.errors:
                key, value = form.errors.popitem()
                messages.error(request, "{}: {}".format(key, value))
            elif ticket_set.errors:
                key, value = ticket_set.errors.popitem()
                messages.error(request, "{}: {}".format(key, value))

    else:
        form = EventFormModel(instance=event)
        ticket_set = TicketFormSet(instance=event)

    return render(request, 'events/create.html', {'form': form, 'formset': ticket_set})


class EventDetailView(DetailView):
    template_name = 'events/detail.html'
    queryset = Event.objects.all()

# class EventCreateView(CreateView):
#     template_name = 'events/create.html'
#     form_class = EventFormModel
