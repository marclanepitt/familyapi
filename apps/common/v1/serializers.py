from rest_framework import serializers
from common.models import Family,Pet, Post
from finances.models import Charge
from finances.v1.serializers import ChargeSerializer
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","first_name","password","date_of_birth", "pro_pic", "status", "family", "admin","budget_amount","budget_interval")

class FamilySerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)
    class Meta:
        model = Family
        fields = ("id","name", "pro_pic","cover_pic","users")

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "pro_pic", "pet_choice","date_of_birth","family")

class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "pro_pic", "pet_choice","date_of_birth")

    def create(self, validated_data):
        family = Family.objects.get(pk=self.context['family'])
        validated_data['family'] = family
        pet = Pet.objects.create(**validated_data)
        return pet

class PostSerializer(serializers.ModelSerializer):
    charge = ChargeSerializer()
    class Meta:
        model = Post
        fields = ("charge","date","family")