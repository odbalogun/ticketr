from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings


class Discounts(SafeDeleteModel):
    code = models.CharField('code', max_length=50, unique=True)
    percentage = models.IntegerField('percentage', null=True, blank=True)
    amount = models.DecimalField('amount', null=True, blank=True, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    expiry_date = models.DateField('expiry date')
    is_active = models.BooleanField('is active', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def display_discount(self):
        if self.percentage:
            return "{}%".format(self.percentage)
        return "N{}".format(self.amount)

    def __str__(self):
        return self.code