from django.contrib import admin
from .models import Subscribers


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']


admin.site.register(Subscribers, SubscriberAdmin)

