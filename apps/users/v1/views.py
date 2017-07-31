from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from familyapi.permissions import IsSelf
from knox.auth import TokenAuthentication

from . import serializers


class UserDetailView(generics.RetrieveAPIView):
    """
    Return information for a specific user.
    Passing `me` instead of a user pk in the url will return information about the user making the request.
    (i.e. The currently authenticated user)
    """

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSelf)
    #authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.UserDetailSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            return get_object_or_404(User, pk=self.request.user.id)
        return super().get_object()


class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
