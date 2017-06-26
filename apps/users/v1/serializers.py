from django.contrib.auth.models import User
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'username', 'last_login', 'is_active',
                  'date_joined')
