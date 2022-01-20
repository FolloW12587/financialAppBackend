from django.db.models import fields
from rest_framework import serializers

from . import models


class FinancialUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinancailUnitsType
        fields = ['name']


class FinancialUnitSerializer(serializers.ModelSerializer):
    fin_type = FinancialUnitTypeSerializer()

    class Meta:
        model = models.FinancialUnit
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        exclude = ['desc']

# class SettingsSerializer(serializers.BaseSerializer):
#     def to_representation(self, instance):
#         if instance.settings_type == models.Settings.INT:
#             value = int(instance.value)

#         elif instance.settings_type == models.Settings.DOUBLE:
#             value = float(instance.value)

#         elif instance.settings_type == models.Settings.LIST:
#             value = instance.value.split(',')

#         else: 
#             value = instance.value

#         return {
#             'id': instance.id,
#             'name': instance.name,
#             'settings_type': instance.settings_type,
#             'value': value
#         }