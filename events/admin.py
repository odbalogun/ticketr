from django.contrib import admin
from .models import Event, Venue, Category, Ticket


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('name', 'slug', 'created_at')


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'state')


admin.site.register(Venue, VenueAdmin)
admin.site.register(Event)
admin.site.register(Category, CategoryAdmin)