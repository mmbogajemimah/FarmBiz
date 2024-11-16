from django.urls import path
from .views import *

urlpatterns = [
    # AUTHENTICATION
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('confirm-email/', CustomEmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('confirm-email/<slug:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),
    path('inactive-logout/', InactiveLogoutView.as_view(), name='inactive_logout'),
    path('password/reset/key/<uidb36>/<key>/', CustomPasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    path('accounts/password/reset/key/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    
    
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('farmer/dashboard/', FarmerDashboardView.as_view(), name='farmer_dashboard'),
    path('business_owner/dashboard/', BusinessOwnerDashboardView.as_view(), name='business_owner_dashboard'),
    path('dashboard/', DefaultDashboardView.as_view(), name='default_dashboard'),  # Fallback dashboard
]

