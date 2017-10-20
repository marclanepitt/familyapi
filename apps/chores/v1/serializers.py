from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404
from users.v1.serializers import UserProfileSerializer
from common.v1.serializers import PetSerializer
from users.models import UserProfile
from common.models import Pet

from ..models import Chore

class ChoreCreateSerializer(serializers.ModelSerializer):
    pass

class ChoreListSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(many=True,read_only=True)
    pets = PetSerializer(many=True,read_only=True)
    class Meta:
        model= Chore
        fields=("id","family","created_by","name","days","date_start","time_start","time_end","is_completed","num_points","repeat","participants","pets","completed_date","redeemed_date")

class ChoreUpdateSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserProfile.objects.all())
    pets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Pet.objects.all())
    class Meta:
        model= Chore
        fields=("id","family","created_by","name","days","time_start","time_end","is_completed","num_points","repeat","participants","pets","completed_date","redeemed_date")