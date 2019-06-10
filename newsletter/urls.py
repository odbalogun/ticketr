from django.urls import path, include
from .views import SubscriberCreateView

app_name = 'newsletter'

# subscriber_views = SubscribersViews()

urlpatterns = [
    # path('', include(subscriber_views.get_urls())),
    path('signup/', SubscriberCreateView.as_view(), name='signup'),
]
