from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from . import serializers, models


class FinancialUnitsView(ReadOnlyModelViewSet):
    queryset = models.FinancialUnit.objects.filter(active=True).all()
    serializer_class = serializers.FinancialUnitSerializer
    permission_classes = [AllowAny, ]

    # def get_queryset(self):
    #     queryset = self.queryset
    #     appId = self.request.query_params.get('appId')
    #     if appId is not None:
    #         return queryset.filter(app__id=appId)
    #     else:
    #         return queryset.none()


class SettingsView(ReadOnlyModelViewSet):
    queryset = models.Settings.objects.filter(app__name='Займы онлайн').all()
    serializer_class = serializers.SettingsSerializer
    permission_classes = [AllowAny, ]


class SettingsMexicaView(ReadOnlyModelViewSet):
    queryset = models.Settings.objects.filter(app__name='Préstamos Personales').all()
    serializer_class = serializers.SettingsSerializer
    permission_classes = [AllowAny, ]


class LeadFormDataView(ModelViewSet):
    queryset = models.LeadFormData.objects.all()
    serializer_class = serializers.LeadFormDataSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['post', ]
