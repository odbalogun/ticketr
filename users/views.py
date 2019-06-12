from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import UserModelForm
from .models import User


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    success_url = settings.LOGIN_REDIRECT_URL


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context
    # def get_queryset(self):
    #     return User.objects.filter(pk=self.request.user.pk).all()


# class UserListView(ListView):
#     template_name = "users/list.html"
#     queryset = User.objects.all()
#
#
# class UserCreateView(CreateView):
#     form_class =  UserModelForm
#     template_name = "users/create.html"
#     success_url = reverse_lazy("users:login")
#
#     def form_valid(self, form):
#         self.object = User.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'],
#                                                first_name=form.cleaned_data['first_name'],
#                                                last_name=form.cleaned_data['last_name'])
#         return HttpResponseRedirect(self.get_success_url())