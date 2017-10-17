from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404
from users.v1.serializers import UserProfileSerializer
from common.v1.serializers import PetSerializer

from ..models import Chore

class ChoreCreateSerializer(serializers.ModelSerializer):
    pass

class ChoreListSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(many=True,read_only=True)
    pets = PetSerializer(many=True,read_only=True)
    class Meta:
        model= Chore
        fields=("id","family","created_by","name","days","time","is_completed","num_points","repeat","participants","pets")