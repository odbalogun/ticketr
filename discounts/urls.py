from django.urls import path
from .views import DiscountCreateView, DiscountListView, DiscountDeleteView, DiscountDetailView, DiscountUpdateView

app_name = 'discounts'

urlpatterns = [
    path('', DiscountListView.as_view(), name='list'),
    path('create/', DiscountCreateView.as_view(), name='create'),
    path('<pk>/', DiscountDetailView.as_view(), name='detail'),
    path('<pk>/delete/', DiscountDeleteView.as_view(), name='delete'),
    path('<pk>/update/', DiscountUpdateView.as_view(), name='update'),
]
