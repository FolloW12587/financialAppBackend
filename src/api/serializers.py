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