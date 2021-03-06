from django.urls import path
# from .views import CustomLoginView, UserCreateView, UserListView, CustomLogoutView
from .views import CustomLoginView, CustomLogoutView, ProfileView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    # path('', UserListView.as_view(), name='list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', login_required(ProfileView.as_view()), name='profile')
    # path('create/', UserCreateView.as_view(), name='create'),
]
