from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from users.forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','emp_id','is_staff', 'is_active','first_name','last_name')
    list_filter = ('email', 'emp_id','is_staff', 'is_active','first_name','last_name')
    fieldsets = (
        (None, {'fields': ('email', 'emp_id','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','emp_id', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','emp_id')
    ordering = ('email','emp_id')
admin.site.register(CustomUser,CustomUserAdmin)
