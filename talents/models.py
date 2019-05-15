from django.db import models
from safedelete.models import SafeDeleteModel
from django.conf import settings


class Bookings(SafeDeleteModel):
    start_date_time = models.DateTimeField('from')
    end_date_time = models.DateTimeField('to')
    budget_from = models.DecimalField('budget from', blank=True, max_digits=10, decimal_places=2)
    budget_to = models.DecimalField('budget to', blank=True, max_digits=10, decimal_places=2)
    engagement_scope = models.TextField('engagement scope')
    venue = models.TextField('venue')
    other_details = models.TextField('other details', blank=True)
    is_resolved = models.TextField('is resolved', default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField('created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'bookings'
        verbose_name = 'booking'

    @property
    def display_budget_from(self):
        # return '{:.2f}'.format(self.budget_from)
        return "$%s" % self.budget_from if self.budget_from else ""

    @property
    def display_budget_to(self):
        # return '{:.2f}'.format(self.budget_from)
        return "$%s" % self.budget_to if self.budget_to else ""


class BookingTalents(SafeDeleteModel):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE, related_name='talents')
    name = models.CharField('name', max_length=100)
    industry = models.CharField('industry', max_length=100)

    class Meta:
        verbose_name_plural = 'booking talents'
        verbose_name = 'booking talent'
