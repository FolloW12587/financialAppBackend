from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from . import serializers, models


class FinancialUnitsView(ReadOnlyModelViewSet):
    queryset = models.FinancialUnit.objects.filter(active=True).all()
    serializer_class = serializers.FinancialUnitSerializer
    permission_classes = [AllowAny,]


class SettingsView(ReadOnlyModelViewSet):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializer
    permission_classes = [AllowAny,]


class LeadFormDataView(ModelViewSet):
    queryset = models.LeadFormData.objects.all()
    serializer_class = serializers.LeadFormDataSerializer
    permission_classes = [AllowAny,]
    http_method_names = ['post',]