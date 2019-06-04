from django.contrib import admin
from .models import Cinema, Movie


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('city', 'state')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_price_2d', 'display_price_3d', 'rating')
    list_filter = ('rating', )
    exclude = ('slug', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

    # for prices
    def display_price_2d(self, object):
        return object.display_price_2d

    def display_price_3d(self, object):
        return object.display_price_3d

    display_price_2d.short_description = '2D Price'
    display_price_2d.admin_order_field = 'price_2d'

    display_price_3d.short_description = '3D Price'
    display_price_3d.admin_order_field = 'price_3d'



admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Movie, MovieAdmin)