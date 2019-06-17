from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Order(SafeDeleteModel):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    code = models.CharField('order code', max_length=50)
    status = models.CharField('status', max_length=50, default='open')
    total_price = models.DecimalField('price', decimal_places=2, max_digits=10)
    payment_status = models.CharField('payment status', max_length=50, default='pending')
    payment_reference = models.CharField('payment reference', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.code)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(SafeDeleteModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.IntegerField('quantity')
    price = models.DecimalField('unit price', decimal_places=2, max_digits=10)

    def get_cost(self):
        return self.price * self.quantity

