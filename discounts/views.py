from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from .models import Discounts
from .forms import DiscountForm


class DiscountCreateView(CreateView):
    form_class = DiscountForm
    template_name = "discounts/create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse_lazy("discounts:list"))


class DiscountListView(ListView):
    template_name = "discounts/list.html"
    queryset = Discounts.objects.all()


class DiscountUpdateView(UpdateView):
    form_class = DiscountForm
    model = Discounts
    success_url = reverse_lazy("discounts:list")
    template_name = "discounts/update.html"


class DiscountDetailView(DetailView):
    queryset = Discounts.objects.all()
    template_name = "discounts/detail.html"


class DiscountDeleteView(DeleteView):
    model = Discounts
    template_name = "discounts/confirm_delete.html"
    success_url = reverse_lazy("discounts:list")
