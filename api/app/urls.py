from django.urls import path
from app.views import RegisterView, LoginView, DashboardView


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]