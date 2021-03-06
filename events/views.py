from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.html import strip_tags
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Event, Category, Ticket
from .forms import EventFormModel, TicketFormSet, PurchaseTicketFormSet
from django.views.decorators.http import require_POST
from cart.cart import Cart


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


@require_POST
def purchase_tickets(request):
    cart = Cart(request)
    purchase_form = PurchaseTicketFormSet(request.POST)

    if purchase_form.is_valid():
        for row in purchase_form:
            cd = row.cleaned_data
            print(cd['ticket_id'])
            print(cd['quantity'])
            ticket = get_object_or_404(Ticket, pk=cd['ticket_id'])
            print(cd)
            cart.add(product=ticket, item_type='events', quantity=cd.get('quantity'))

        messages.success(request, "Your ticket(s) have been added to your cart")
        return HttpResponseRedirect(reverse_lazy("cart:checkout"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url=reverse_lazy('pages:sign-in'))
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
            print(form.data['end_time'])
            if form.errors:
                key, value = form.errors.popitem()
                messages.error(request, "{}: {}".format(form.fields[key].label, strip_tags(value)))
            elif ticket_set.errors:
                print(ticket_set.errors)
                key, value = ticket_set.errors.pop().popitem()
                messages.error(request, "{}: {}".format(key, strip_tags(value)))

    else:
        form = EventFormModel(instance=event)
        ticket_set = TicketFormSet(instance=event)

    return render(request, 'events/create.html', {'form': form, 'formset': ticket_set})


class EventDetailView(DetailView):
    template_name = 'events/detail.html'
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_form'] = PurchaseTicketFormSet()
        return context


class EventListView(ListView):
    template_name = 'events/list.html'
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name').all()
        return context


class EventGetListByCategoryView(ListView):
    template_name = 'events/list_by_category.html'
    queryset = Event.objects.all()
    category = None

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return self.queryset.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Call the super method first to get a context
        context = super().get_context_data(**kwargs)
        # Add the category information
        context['category'] = self.category
        return context