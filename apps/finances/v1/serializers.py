from rest_framework import serializers
from ..models import Charge
from datetime import datetime
from common.models import Family
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","first_name","password","date_of_birth", "pro_pic", "status", "family", "admin","budget_amount","budget_interval")

class ChargeSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer()
    class Meta:
        model = Charge
        fields = ("family","id","created_by","description","charge_type", "amount", "location","date")

class ChargeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ("created_by","description","charge_type","amount","location")

    def create(self, validated_data):
        family = Family.objects.get(pk=self.context['family'])
        validated_data['family'] = family
        charge = Charge.objects.create(**validated_data)
        return charge

