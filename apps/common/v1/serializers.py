from rest_framework import serializers
from common.models import Family,Pet


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "pro_pic")

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "pro_pic", "pet_choice","date_of_birth","family")
