from django.urls import path
from .views import create_event, EventDetailView

app_name = 'events'

urlpatterns = [
    path('create/', create_event, name='create'),
    path('<pk>/', EventDetailView.as_view(), name='detail'),
]
