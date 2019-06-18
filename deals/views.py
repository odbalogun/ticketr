from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from .forms import DealForm, DealCategoriesFormSet
from .models import Deals, DealCategories
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import PurchaseDealForm


@require_POST
def purchase_tickets(request):
    cart = Cart(request)
    form = PurchaseDealForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        ticket = get_object_or_404(DealCategories, pk=cd['deal_id'])
        cart.add(product=ticket, item_type='deals', quantity=cd.get('quantity'))

        messages.success(request, "Your deals have been added to your cart")
        return HttpResponseRedirect(reverse_lazy("cart:checkout"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class DealCreateView(CreateView):
    form_class = DealForm
    template_name = "deals/create.html"
    object = None
    # success_url = reverse_lazy("deals:manage-options", deal_id=object.id)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse_lazy("deals:manage-options", kwargs={'deal_id': self.object.pk}))


class DealListView(ListView):
    template_name = "deals/list.html"
    queryset = Deals.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PurchaseDealForm()
        return context


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