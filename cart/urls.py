from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='checkout'),
    path('add/<product_id>', views.cart_add, name='add'),
    path('remove/<item_type>/<product_id>', views.cart_remove, name='remove'),
]