from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404


from users.models import UserProfile
from common.models import Family
from common.v1.serializers import FamilySerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","first_name","password","date_of_birth", "pro_pic", "status", "family", "admin","budget_amount","budget_interval")

class UserProfileLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    password = serializers.CharField(max_length=4)

    def validate(self, attrs):
        id = attrs.get('id')
        password = attrs.get('password')
        user = get_object_or_404(UserProfile,pk=id)
        if(password == user.password):
            attrs['user'] = user
            return attrs
        else:
            raise exceptions.APIException("Wrong password")


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    family = FamilySerializer()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('family','id', 'first_name', 'last_name', 'full_name', 'email', 'username', 'last_login', 'is_active',
                  'date_joined',)


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    family = FamilySerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def custom_signup(self, request, user):
        family_data = self.validated_data.get('family', {})
        family_data['user'] = user
        Family.objects.create(**family_data)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = data.get('email')
        data['first_name'] = self.validated_data.get('first_name')
        data['last_name'] = self.validated_data.get('last_name')
        return data
