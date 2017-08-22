from rest_framework import serializers
from ..models import Charge

class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ("created_by","description","charge_type", "amount", "location")