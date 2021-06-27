from django.urls import path
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from .views import MyTokenObtainPairView, MyRegisterView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', MyRegisterView.as_view(), name='register'),
]