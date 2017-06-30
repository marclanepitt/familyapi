from django.contrib.auth.models import User
from common.models import Institution
from users.models import UserProfile
from rest_framework import serializers
from common.v1.serializers import InstitutionSerializer,MajorSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    major = MajorSerializer()
    class Meta:
        model = UserProfile
        fields = ('year', 'institution', 'major')

class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    userprofile = UserProfileSerializer()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'username', 'last_login', 'is_active',
                  'date_joined', 'userprofile')
