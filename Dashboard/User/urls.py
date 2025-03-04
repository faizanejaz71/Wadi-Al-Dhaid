from django.urls import path
from .views import UserSignupView, UserLoginView, PasswordResetRequestView, PasswordResetConfirmView

urlpatterns = [

    # User Authentication URLs
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    # Password Reset URLs
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
 