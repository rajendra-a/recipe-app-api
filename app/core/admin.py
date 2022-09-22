from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _ 

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the pages for the admin users"""
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email","password")}),
        (
            _("permissions"),
            {
            'fields':(
                'is_active',
                'is_staff',
                'is_superuser',
                )
            }

        )
    )
    


admin.site.register(models.User, UserAdmin)
