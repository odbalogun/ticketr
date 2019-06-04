from django.urls import path
from .views import HomePageView, SignupPageView, VerifyEmailView, TestPageView, LoginPageView, LogoutPageView, \
    ProfilePageView, CheckoutPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', HomePageView.as_view(), name='home'),
    path('talent/', TestPageView.as_view(), name='talent'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('verify-email/<email>', VerifyEmailView.as_view(), name='verify')
]
