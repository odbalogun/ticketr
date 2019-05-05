from django.urls import path
from .views import DealCreateView, DealListView, manage_deal_categories

app_name = 'deals'

urlpatterns = [
    path('', DealListView.as_view(), name='list'),
    path('create/', DealCreateView.as_view(), name='create'),
    path('<deal_id>/manage-options/', manage_deal_categories, name='manage-options')
]
