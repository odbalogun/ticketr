from django.urls import path
from .views import create_event, EventDetailView, EventListView, EventGetListByCategoryView, search_events

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('category/<category_slug>', EventGetListByCategoryView.as_view(), name='list-by-category'),
    path('create/', create_event, name='create'),
    path('search/', search_events, name='search'),
    path('<pk>/', EventDetailView.as_view(), name='detail'),
]
