from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import UserSerializer


class RegisterUser(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny 
    ]
    serializer_class = UserSerializer