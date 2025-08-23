from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # completely remove the field

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
        }

class CustomLoginSerializer(LoginSerializer):
    username = None  # completely remove the field
    
    def get_cleaned_data(self):
        return{
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
        }