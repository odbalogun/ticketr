from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from .forms import DealForm, DealCategoriesFormSet
from .models import Deals, DealCategories


class DealCreateView(CreateView):
    form_class = DealForm
    template_name = "deals/create.html"
    # success_url = reverse_lazy("deals:manage-options", deal_id=object.id)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse_lazy("deals:manage-options", kwargs={'deal_id':self.object.pk}))


class DealListView(ListView):
    template_name = "deals/list.html"
    queryset = Deals.objects.all()


class DealUpdateView(UpdateView):
    form_class = DealForm
    model = Deals
    success_url = reverse_lazy("deals:list")
    template_name = "deals/update.html"


class DealDetailView(DetailView):
    queryset = Deals.objects.all()
    template_name = "deals/detail.html"


class DealDeleteView(DeleteView):
    model = Deals
    template_name = "deals/confirm_delete.html"
    success_url = reverse_lazy("deals:list")


def manage_deal_categories(request, deal_id):
    deal = Deals.objects.get(pk=deal_id)

    if request.method == 'POST':
        formset = DealCategoriesFormSet(request.POST, request.FILES, instance=deal)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('deals:list'))
        else:
            return render(request, 'deals/options/create_list.html', {'formset': formset})

    formset = DealCategoriesFormSet(queryset=DealCategories.objects.filter(deal__id=deal.pk))
    return render(request, 'deals/options/create_list.html', {'formset': formset})