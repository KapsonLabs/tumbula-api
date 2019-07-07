from django.urls import path, include
from .views import LoginView, RegisterView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterView.as_view(), name="auth-register"),
]