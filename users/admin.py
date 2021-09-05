from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    readonly_fields = ('unique_id',)

    fieldsets = (
        # *BaseUserAdmin.fieldsets,    # original form fieldsets, expanded
        # new fieldset added on to the bottom
        (
            '',                                         # Group Heading
            {'fields': ['username', 'password']},       # Group Fields
        ),
        (
            'Personal info',
            {'fields': ['unique_id', 'first_name', 'last_name', 'mobile', 'email']},
        ),
        (
            'Permissions',
            {'fields': ['is_active', 'is_staff', 'is_superuser',
                        'groups', 'user_permissions'], 'classes': ['collapse']}
        ),
        (
            'Important dates',
            {'fields': ['last_login', 'date_joined']}
        )
    )


admin.site.register(User, UserAdmin)
