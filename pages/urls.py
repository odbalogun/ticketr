from django.urls import path
from .views import HomePageView, SignupPageView, VerifyEmailView, TestPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', HomePageView.as_view(), name='home'),
    path('talent/', TestPageView.as_view(), name='talent'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('verify-email/<email>', VerifyEmailView.as_view(), name='verify')
]
