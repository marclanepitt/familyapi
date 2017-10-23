from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from knox.auth import TokenAuthentication
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status

from familyapi.permissions import IsSelf
from . import serializers
from ..models import UserProfile

class UserDetailView(generics.RetrieveAPIView):
    """
    Return information for a specific user.
    Passing `me` instead of a user pk in the url will return information about the user making the request.
    (i.e. The currently authenticated user)
    """

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSelf)
    serializer_class = serializers.UserDetailSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            return get_object_or_404(User, pk=self.request.user.id)
        return super().get_object()


class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileListView(generics.ListAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.kwargs['id'])

class RegistrationView(RegisterView):
    def get_response_data(self, user):
        data = super().get_response_data(user)
        data.update({"family":user.family.id,"admin":"SU"})
        return data

class UserProfileLoginView(generics.GenericAPIView):
    serializer_class = serializers.UserProfileLoginSerializer

    def get_response(self):

        data = {
                'status': 1,
                }

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        return self.get_response()

class UserProfileUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)