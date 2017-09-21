from rest_framework import serializers
from common.models import Family,Pet
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","first_name","password","date_of_birth", "pro_pic", "status", "family", "admin")
class FamilySerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)
    class Meta:
        model = Family
        fields = ("id","name", "pro_pic","users")

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "pro_pic", "pet_choice","date_of_birth","family")
