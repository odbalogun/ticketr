from django.contrib import admin
from .models import Bookings


# create admin models
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'display_budget_from', 'display_budget_to', 'start_date_time', 'end_date_time',
                    'is_resolved', 'created_at')
    list_filter = ('created_by', 'created_at')



# Register your models here.
admin.site.register(Bookings, BookingsAdmin)
# admin.site.register(BookingTalents)