from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from knox.auth import TokenAuthentication
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ChoreListSerializer
from ..models import Chore

class ChoreListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family)
class ChoreListUserView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        user_profile = self.kwargs['user_profile']
        return Chore.objects.filter(family=family,participants=user_profile)

class ChoreAvailableListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family, participants=None)

class ChoreUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Chore.objects.all()
    serializer_class = ChoreListSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)