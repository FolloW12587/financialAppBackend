from django.urls import path
from . import views

urlpatterns = [
    path('policy/', views.terms, name='policy'),
    path('', views.support, name='support'),
]