from django.urls import path
from .views import CustomLoginView, UserCreateView, UserListView, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name='create'),
]
