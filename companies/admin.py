from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Company


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'companies'


class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Company)