from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import Event, Category
from .forms import EventFormModel, TicketFormSet


def search_events(request):
    search_term, location = request.GET.get('q'), request.GET.get('location')
    qs = Event.objects
    filters = False

    if search_term:
        filters = Q(title__icontains=search_term)
        if location:
            filters = filters & (Q(venue__name__icontains=location) | Q(venue__street__icontains=location)
                                 | Q(venue__city__icontains=location))

    if filters:
        qs = qs.filter(filters)

    return render(request, 'events/search.html', {'object_list': qs.all(), 'search_term': search_term,
                                                  'location': location})


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


class EventListView(ListView):
    template_name = 'events/list.html'
    queryset = Event.objects.all()


class EventGetListByCategoryView(ListView):
    template_name = 'events/list_by_category.html'
    queryset = Event.objects.all()

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return self.queryset.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Call the super method first to get a context
        context = super().get_context_data(**kwargs)
        # Add the category information
        context['category'] = self.category
        return context