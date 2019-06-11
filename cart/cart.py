from decimal import Decimal
from django.conf import settings
from deals.models import DealCategories
from events.models import Ticket
from movies.models import Movie


class Cart(object):
    item_types = ['events', 'movies', 'deals']

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {'events': {}, 'movies': {}, 'deals': {}}
        self.cart = cart

    def add(self, product, item_type, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        if item_type not in self.item_types:
            raise TypeError("Invalid item type: {}".format(item_type))

        product_id = str(product.id)
        if product_id not in self.cart[item_type]:
            self.cart[item_type][product_id] = {'quantity': 0, 'price': product.price}

        if update_quantity:
            self.cart[item_type][product_id]['quantity'] = quantity
        else:
            self.cart[item_type][product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product, item_type):
        """
        Remove a product from the cart.
        """
        if item_type not in self.item_types:
            raise TypeError("Invalid item type: {}".format(item_type))
        product_id = str(product.id)
        if product_id in self.cart[item_type]:
            del self.cart[item_type][product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        for item_type in self.cart.keys():
            product_ids = self.cart[item_type].keys()

            if item_type == 'movies':
                products = Movie.objects.filter(id__in=product_ids)
            elif item_type == 'events':
                products = Ticket.objects.filter(id__in=product_ids)
            elif item_type == 'deals':
                products = DealCategories.objects.filter(id__in=product_ids)
            else:
                raise TypeError("Invalid item type: {}".format(item_type))

            # get the product objects and add them to the cart
            for product in products:
                self.cart[item_type][str(product.id)]['product'] = product

        for key in self.cart.keys():
            for item in self.cart[key].values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item
