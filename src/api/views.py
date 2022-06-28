from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models.query import QuerySet

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

    def list(self, request):
        queryset = self.get_queryset()
        queryset: QuerySet

        # isAppsflyerActive = queryset.filter(name="isAppsflyerActive").first()
        # appsFlyerCounterMax = queryset.filter(
        #     name="appsFlyerCounterMax").first()
        # appsFlyerCounter = queryset.filter(name="appsFlyerCounter").first()
        queryset = queryset.exclude(
            name__in=["appsFlyerCounterMax", "appsFlyerCounter"])

        # if not isAppsflyerActive or not appsFlyerCounter or not appsFlyerCounterMax:
        #     serializer = self.serializer_class(queryset, many=True)
        #     return Response(serializer.data)

        # try:
        #     appsFlyerCounter.value = str(int(appsFlyerCounter.value) + 1)
        #     if int(appsFlyerCounter.value) >= int(appsFlyerCounterMax.value):
        #         appsFlyerCounter.value = '0'
        #         isAppsflyerActive.value = '1'
        #     else:
        #         isAppsflyerActive.value = '0'
        # except ValueError:
        #     serializer = self.serializer_class(queryset, many=True)
        #     return Response(serializer.data)

        # isAppsflyerActive.save()
        # appsFlyerCounter.save()

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class SettingsMexicaView(ReadOnlyModelViewSet):
    queryset = models.Settings.objects.filter(
        app__name='Préstamos Personales').all()
    serializer_class = serializers.SettingsSerializer
    permission_classes = [AllowAny, ]


class LeadFormDataView(ModelViewSet):
    queryset = models.LeadFormData.objects.all()
    serializer_class = serializers.LeadFormDataSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['post', ]
