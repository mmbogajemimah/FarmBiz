from django.contrib import admin
from accounts.models import AdminUser, FarmerUser, BusinessOwnerUser

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_no')

@admin.register(FarmerUser)
class FarmerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_no')

@admin.register(BusinessOwnerUser)
class BusinessOwnerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_no')
