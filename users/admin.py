from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                'avatar',
                'gender',
                'bio',
                'language',
                'currency',
                'superhost'
            ),
        }),
    )

    list_filter = UserAdmin.list_filter + (
        'superhost',
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser'
        )
    

