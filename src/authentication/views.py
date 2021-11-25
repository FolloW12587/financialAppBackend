from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import UserSerializer


class RegisterUser(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny 
    ]
    serializer_class = UserSerializer


class TestLogin(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        content = {'success': True}
        return Response(content)