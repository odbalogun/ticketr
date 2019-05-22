from django.contrib import admin
from .models import Deals, DealCategories
from .forms import DealCategoriesInlineFormSet


# create admin models
class DealCategoriesInline(admin.StackedInline):
    model = DealCategories
    formset = DealCategoriesInlineFormSet
    max_num = 4
    extra = 4
    can_delete = False
    exclude = ('available_quantity',)


class DealAdmin(admin.ModelAdmin):
    inlines = [
        DealCategoriesInline,
    ]

    list_display = ('name', 'slug', 'expiry_date', 'is_active', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    exclude = ('slug', 'created_at', 'created_by')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()


# Register your models here.
admin.site.register(Deals, DealAdmin)