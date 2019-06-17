from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .cart import Cart
from .forms import CartAddItemForm
from events.models import Ticket
# from movies.models import Movie
from deals.models import DealCategories


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        if cd['item_type'] == 'events':
            product = get_object_or_404(Ticket, id=product_id)
        else:
            product = get_object_or_404(DealCategories, id=product_id)

        cart.add(product=product, item_type=cd['item_type'], quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, "Item has been successfully updated")
    return redirect('cart:checkout')


def cart_remove(request, item_type, product_id):
    cart = Cart(request)

    if item_type == 'events':
        product = get_object_or_404(Ticket, id=product_id)
    else:
        product = get_object_or_404(DealCategories, id=product_id)

    cart.remove(product, item_type=item_type)
    return redirect('cart:checkout')


def cart_detail(request):
    cart = Cart(request)

    if len(cart) == 0:
        messages.error(request, 'There are no items in your cart')
        return redirect('pages:home')

    for item in cart:
        item['update_quantity_form'] = CartAddItemForm(initial={'quantity': item['quantity'],
                                                                'item_type': item['item_type'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})