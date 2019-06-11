from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings


class Cart(SafeDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField('created at', auto_now_add=True)