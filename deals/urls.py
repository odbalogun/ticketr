from django.urls import path
from .views import DealCreateView, DealListView, manage_deal_categories, DealDeleteView, DealDetailView, DealUpdateView

app_name = 'deals'

urlpatterns = [
    path('', DealListView.as_view(), name='list'),
    path('create/', DealCreateView.as_view(), name='create'),
    path('<pk>/', DealDetailView.as_view(), name='detail'),
    path('<pk>/delete/', DealDeleteView.as_view(), name='delete'),
    path('<pk>/update/', DealUpdateView.as_view(), name='update'),
    path('<deal_id>/manage-options/', manage_deal_categories, name='manage-options')
]
