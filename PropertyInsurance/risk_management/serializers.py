
from rest_framework import serializers
from risk_management.models import Risks,RisksType,RisksSubType


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risks
        fields = ('id', 'Name', 'code',)


class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RisksType
        fields = ('id', 'Name', 'code','risk')


class RiskSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RisksSubType
        fields = ('id', 'Name', 'code','risk_type')

