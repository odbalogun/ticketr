from django.views.generic import CreateView
from .forms import SubscriberForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

# from cruds_adminlte.crud import CRUDView
# class SubscribersViews(CRUDView):
#     model = Subscribers
#     namespace = 'newsletter'
#     check_login = False
#     check_perms = False


class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    template_name = "newsletter/_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, "Thank you for signing up for our newsletter!")

        return HttpResponseRedirect(reverse_lazy("pages:home"))
