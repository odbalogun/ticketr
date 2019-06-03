from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Client


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'created_at')
    list_filter = ('is_superuser', 'created_at', 'is_active')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company', 'created_at')

    def get_queryset(self, request):
        return self.model.objects.filter(is_staff=False)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.unregister(Group)