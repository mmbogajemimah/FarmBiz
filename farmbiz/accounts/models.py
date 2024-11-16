from django.contrib.auth.models import AbstractUser
from django.db import models

################## Custom User Model  Captures Users' Details ###################
class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    USER_TYPES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmers'),
        ('business_owner', 'Business Owner'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPES, default='farmer')

    # Add the password_needs_reset field with a default of False
    password_needs_reset = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    
############# Proxy models for the various user types in the system ####################

class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='admin')


class FarmerUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='farmer')


class BusinessOwnerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='business_owner')


class AdminUser(CustomUser):
    objects = AdminUserManager()

    class Meta:
        proxy = True
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"

    def admin_specific_method(self):
        return f"Admin: {self.username}"


class FarmerUser(CustomUser):
    objects = FarmerUserManager()

    class Meta:
        proxy = True
        verbose_name = "Farmer User"
        verbose_name_plural = "Farmer Users"

    def farmer_specific_method(self):
        return f"Farmer: {self.username}"


class BusinessOwnerUser(CustomUser):
    objects = BusinessOwnerManager()

    class Meta:
        proxy = True
        verbose_name = "Business Owner"
        verbose_name_plural = "Business Owners"

    def business_owner_specific_method(self):
        return f"Business Owner: {self.username}"


