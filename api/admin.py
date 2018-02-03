from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

# Register your models here.
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """ The forms to add and change user instances """
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    """
    The fields to be used in displaying the User model.
    These override the definitions on the base UserAdmin
    that reference specific fields on auth.User."""
    list_display = ('email', 'username', 'superuser')
    list_filter = ('superuser', 'staff', 'active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Username', {'fields': ('username',)}),
        ('Permissions', {'fields': ('superuser', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
