from rest_framework import serializers
from common.models import Family


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "pro_pic")
