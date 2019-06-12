from django.urls import path
from .views import HomePageView, SignupPageView, VerifyEmailView, LoginPageView, LogoutPageView, \
    CheckoutPageView, EventPageView, StandaloneLoginPageView, StandaloneSignupPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', HomePageView.as_view(), name='home'),
    path('sign-in/', StandaloneLoginPageView.as_view(), name='sign-in'),
    path('register/', StandaloneSignupPageView.as_view(), name='register'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
    path('event/', EventPageView.as_view(), name='event'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('verify-email/<email>', VerifyEmailView.as_view(), name='verify')
]
