from rest_framework import serializers
from ..models import Charge
from datetime import datetime
from common.models import Post,Family
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","first_name","password","date_of_birth", "pro_pic", "status", "family", "admin")

class ChargeSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer()
    class Meta:
        model = Charge
        fields = ("family","id","created_by","description","charge_type", "amount", "location")

class ChargeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ("created_by","description","charge_type","amount","location")

    def create(self, validated_data):
        family = Family.objects.get(pk=self.context['family'])
        validated_data['family'] = family
        post = Post.objects.create(date=datetime.now(), family =family)
        validated_data["post"] = post
        charge = Charge.objects.create(**validated_data)
        return charge

