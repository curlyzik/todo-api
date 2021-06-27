from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import (
        UserModelSerializer, MyTokenObtainPairSerializer,
        MyRegisterSerializer,
)

User = get_user_model()

# OBTAINING A TOKEN WHEN USER IS LOGGED IN
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyRegisterView(RegisterView):
    serializer_class = MyRegisterSerializer