from rest_framework import serializers
from ..models import Charge
from common.v1.serializers import PostSerializer
from common.models import Post

class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ("family","id","created_by","description","charge_type", "amount", "location")