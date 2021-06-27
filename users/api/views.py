from rest_framework_simplejwt.views import TokenObtainPairView
from dj_rest_auth.registration.views import RegisterView
from django.contrib.auth import get_user_model

from .serializers import MyTokenObtainPairSerializer, MyRegisterSerializer,

User = get_user_model()

# LOG IN A USER
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# REGISTER A USER
class MyRegisterView(RegisterView):
    serializer_class = MyRegisterSerializer