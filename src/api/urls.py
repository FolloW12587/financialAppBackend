from django.urls import path
from . import views

urlpatterns = [
    path('financial_units/', views.FinancialUnitsView.as_view({'get': 'list'}), name='financial_units'),
]