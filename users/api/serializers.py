from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from allauth.account import app_settings as allauth_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

User = get_user_model()

# Serializer for Users
class UserModelSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'isAdmin']

    def get_isAdmin(self, obj):
        isAdmin = obj.is_staff
        return isAdmin

# Serializer for Log In
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField()

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserModelSerializer(self.user).data
        for k,v in serializer.items():
            data[k] = v

        return data

class MyRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )