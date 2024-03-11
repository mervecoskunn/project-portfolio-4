from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_full_name', 'username',
        'email', 'is_active', 'is_staff',
        'is_superuser', 'date_joined', 'last_login'
    )
    list_filter = (
        'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login'
    )
    search_fields = ('username', 'first_name',
                     'last_name', 'email')
    search_help_text = _(f"Searchable by username, first_name, last_name, email fields")

    ordering = ('id',)

    def get_readonly_fields(self, request, obj=None):
        _fields = ('username', 'password', 'date_joined', 'last_login')
        readonly_list = []
        if obj is not None and request.user.is_superuser is False:
            readonly_list.extend([obj._meta.get_field(field_name).name for field_name in _fields if
                                  getattr(obj, field_name) is not None])
        return readonly_list
