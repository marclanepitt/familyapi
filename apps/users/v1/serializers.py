from django.contrib.auth.models import User

from users.models import UserProfile
from rest_framework import serializers

from rest_auth.registration.serializers import RegisterSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    userprofile = UserProfileSerializer()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'username', 'last_login', 'is_active',
                  'date_joined', 'userprofile')


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    user_profile = UserProfileSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def custom_signup(self, request, user):
        user_profile_data = self.validated_data.get('user_profile', {})
        user_profile_data['user'] = user
        user_profile = UserProfile.objects.create(**user_profile_data)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = data.get('email')
        data['first_name'] = self.validated_data.get('first_name')
        data['last_name'] = self.validated_data.get('last_name')
        return data
