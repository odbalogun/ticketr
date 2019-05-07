from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings


class Bookings(SafeDeleteModel):
    start_date_time = models.DateTimeField('from')
    end_date_time = models.DateTimeField('to')
    budget_from = models.DecimalField('from', blank=True, max_digits=10, decimal_places=2)
    budget_to = models.DecimalField('to', blank=True, max_digits=10, decimal_places=2)
    engagement_scope = models.TextField('engagement scope')
    venue = models.TextField('venue')
    other_details = models.TextField('other details', blank=True)
    resolution = models.TextField('resolved?', null=True, default=None)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class BookingTalents(SafeDeleteModel):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE, related_name='talents')
    name = models.CharField('name', max_length=100)
    industry = models.CharField('industry', max_length=100)

