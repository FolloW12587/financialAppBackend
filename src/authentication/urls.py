from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('test_login/', views.TestLogin.as_view(), name='test_login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]