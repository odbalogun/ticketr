from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Cart(SafeDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField('order code', max_length=50)
    status = models.CharField('status', max_length=50, default='open')
    created_at = models.DateTimeField('created at', auto_now_add=True)


class CartItems(SafeDeleteModel):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')