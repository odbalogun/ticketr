from django.contrib import admin
from .models import Discounts


# create admin models
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'display_discount', 'expiry_date', 'is_active', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    exclude = ('created_by', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()


# Register your models here.
admin.site.register(Discounts, DiscountAdmin)