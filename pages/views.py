from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth import login
from .forms import VerificationCodeForm
from deals.models import Deals
from events.models import Category as EventCategory, Event
from users.models import User
from users.forms import SignUpModelForm
from django.conf import settings


class TestPageView(TemplateView):
    template_name = "pages/talent.html"

class ProfilePageView(TemplateView):
    template_name = "pages/profile.html"

class CheckoutPageView(TemplateView):
    template_name = "pages/checkout.html"

class EventPageView(TemplateView):
    template_name = "pages/event.html"


class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):
        context = {
            'deal': Deals.objects.last(),
            'categories': EventCategory.objects.all()[:6],
            'events': Event.objects.filter(image__isnull=False).order_by('-created_at')[:4]
        }

        return render(request, 'pages/index.html', context)


class LoginPageView(LoginView):
    # success_url = reverse_lazy("users:profile")
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = "pages/_login.html"

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy("pages:home"))

    def form_invalid(self, form):
        # messages.error(self.request, "There were errors in your form")
        key, value = form.errors.popitem()
        messages.error(self.request, "{}: {}".format(key, value))
        return redirect(reverse_lazy("pages:home"))


class LogoutPageView(LogoutView):
    template_name = 'pages/_logout.html'
    next_page = reverse_lazy("pages:home")


class SignupPageView(FormView):
    form_class = SignUpModelForm
    template_name = 'pages/_signup.html'
    email = None

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy("pages:home"))

    def get_success_url(self):
        return reverse_lazy('pages:verify', kwargs={'email': self.email})

    def form_valid(self, form):
        email = form.cleaned_data.pop('email')
        password = form.cleaned_data.pop('password')

        # set extra variables
        form.cleaned_data['is_active'] = False
        form.cleaned_data['is_staff'] = False

        user = User.objects.create_user(email, password, **form.cleaned_data)
        # send email
        user.email_user(subject='Ticketr verification code',
                        message='This is your verification code: {}'.format(user.verification_code))
        messages.success(self.request, "A verification code has been sent to your email")
        self.email = user.email
        return super(SignupPageView, self).form_valid(form)
        # return reverse_lazy("pages:verify", kwargs={'email': user.email})

    def form_invalid(self, form):
        messages.error(self.request, "There were errors in your form")
        return redirect(reverse_lazy("pages:home"))


class VerifyEmailView(FormView):
    form_class = VerificationCodeForm
    success_url = reverse_lazy("users:profile")
    template_name = "pages/verify_email.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'email': kwargs['email']})
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        try:
            user = User.objects.get(email=form.cleaned_data['email'])
        except User.DoesNotExist:
            user = None

        if user:
            # todo if user.verification_code == form.cleaned_data['verification_code']:
            if True:
                if not user.is_active:
                    user.email_user(subject='Welcome to Ticketr!', message='Your account has been successfully verified')
                    user.is_active = True
                    user.save()
                    login(self.request, user)
                return super().form_valid(form)
            else:
                messages.error(self.request, "Invalid email and verification code combination")
        else:
            messages.error(self.request, "No such user exists")

        return self.form_invalid(form)
