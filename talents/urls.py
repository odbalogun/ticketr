from django.urls import path
from .views import create_talent_booking, TalentListView, TalentDeleteView, TalentDetailView
from django.contrib.auth.decorators import login_required

app_name = 'talents'

urlpatterns = [
    path('bookings/', TalentListView.as_view(), name='list-bookings'),
    path('bookings/create/', login_required(create_talent_booking), name='create-booking'),
    path('bookings/<pk>/', TalentDetailView.as_view(), name='view-booking'),
    path('bookings/<pk>/delete/', TalentDeleteView.as_view(), name='delete-booking'),
]
