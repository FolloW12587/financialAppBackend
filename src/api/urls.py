from django.urls import path
from . import views

urlpatterns = [
    path('financial_units/', views.FinancialUnitsView.as_view({'get': 'list'}), name='financial_units'),
    path('settings/', views.SettingsView.as_view({'get': 'list'}), name='settings'),
    path('settingsPrestamos/', views.SettingsMexicaView.as_view({'get': 'list'}), name='settingsPrestamos'),
    path('lead_form/', views.LeadFormDataView.as_view({'post': 'create'}), name='lead_form'),
]