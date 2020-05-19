from django.urls import path
from .views import UserRegistrationView, CabinetView

app_name = "users"

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='register'),
    path('accounts/cabinet/', CabinetView.as_view(), name='profile'),
]