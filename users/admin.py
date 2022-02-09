from django.contrib import admin
from users.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User model fields list display"""

    list_display = (
        "id",
        "email",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "id",
        "email",
        "created_on",
        "updated_on",
    )
