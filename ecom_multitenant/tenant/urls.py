from django.urls import path, include
from tenant.views import UserRegistrationView, UserLoginView, UserLogoutView, AddTenantAPI

urlpatterns = [
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/auth/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('api/add/tenant/', AddTenantAPI.as_view(), name='add-tenant'),
    # Add other URLs here
]