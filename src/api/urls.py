from django.urls import path
from . import views

urlpatterns = [
    path('financial_units/', views.FinancialUnitsView, name='financial_units'),
]