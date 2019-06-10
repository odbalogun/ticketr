from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from safedelete import HARD_DELETE_NOCASCADE
from .models import Bookings, Industry
from .forms import BookingTalentFormSet, BookingForm


def create_talent_booking(request):
    if request.method == 'POST':
        # first save form
        form = BookingForm(request.POST)
        # to ensure that formset is also populated
        formset = BookingTalentFormSet(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.created_by = request.user
            # save booking
            booking.save()
            # process formset
            formset = BookingTalentFormSet(request.POST, instance=booking)

            if formset.is_valid():
                formset.save()
                return redirect(reverse_lazy('talents:list-bookings'))
            else:
                booking.delete(force_policy=HARD_DELETE_NOCASCADE)
    else:
        form = BookingForm()
        formset = BookingTalentFormSet()
    return render(request, 'talents/bookings/create.html', {'form': form, 'formset': formset,
                                                            'industries': Industry.objects.all()})


class TalentListView(ListView):
    template_name = "talents/bookings/list.html"
    queryset = Bookings.objects.all()


class TalentDetailView(DetailView):
    queryset = Bookings.objects.all()
    template_name = "talents/bookings/detail.html"


class TalentDeleteView(DeleteView):
    model = Bookings
    template_name = "talents/bookings/confirm_delete.html"
    success_url = reverse_lazy("talents:list-bookings")