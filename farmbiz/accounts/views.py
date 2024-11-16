from django.shortcuts import render, redirect
from allauth.account.views import SignupView, ConfirmEmailView, LoginView, LogoutView, PasswordResetFromKeyView, AccountInactiveView, PasswordChangeView
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages

############ Custom User Sign Up ####################
class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    
    
############ Custom Email Verification ####################
class CustomEmailVerificationSentView(TemplateView):
    template_name = 'account/verification_sent.html'
    
    
############ Custom Email Confirmation ####################
class CustomConfirmEmailView(ConfirmEmailView):
    template_name = 'account/email_confirm.html'


############ Custom Password Reset ####################
class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'account/password_reset_from_key.html'


############ Custom Password Reset Confirmation ####################
class CustomPasswordResetDoneView(TemplateView):
    template_name = 'account/password_reset_done.html'
    
    
##################### Account Inactive View Function ####################
class CustomAccountInactiveView(AccountInactiveView):
    template_name = 'account/account_inactive.html'
    
    
##################### Password Change #####################
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/custom_password_change.html'
    
    
############ Custom User Login and Redirection ####################
class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        # Testing purposes
        print("I got the form")
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Testing purposes
            print("I got the redirection")

            # Check the user type and redirect accordingly
            if user.user_type == 'admin':
                return redirect('admin_dashboard')  # You should have a URL named 'admin_dashboard'
            elif user.user_type == 'farmer':
                return redirect('farmer_dashboard')  # You should have a URL named 'farmer_dashboard'
            elif user.user_type == 'business_owner':
                return redirect('business_owner_dashboard')  # You should have a URL named 'business_owner_dashboard'
            else:
                return redirect('default_dashboard')  # Default redirect if the user type is unknown
        else:
            print("Login failed")
        
        return render(request, 'account/login.html', {'form': form})
    
##################### LogOut View #####################
class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'

##################### Inactive LogOut View #####################
class InactiveLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "You have been logged out due to inactivity.")
        return redirect('account_login')
    
    
    
# Admin Dashboard View
class AdminDashboardView(TemplateView):
    template_name = 'dashboard/admin_dashboard.html'
    
    # Optionally, you can override the get_context_data method to add extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'admin'
        return context

# Farmer Dashboard View
class FarmerDashboardView(TemplateView):
    template_name = 'dashboard/farmer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'farmer'
        return context

# Business Owner Dashboard View
class BusinessOwnerDashboardView(TemplateView):
    template_name = 'dashboard/business_owner_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'business_owner'
        return context

# Default Dashboard View (Fallback)
class DefaultDashboardView(TemplateView):
    template_name = 'dashboard/default_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'default'
        return context