from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from knox.auth import TokenAuthentication
from rest_framework import generics,mixins
from users.models import UserProfile

from .serializers import ChoreListSerializer,ChoreUpdateSerializer
from ..models import Chore

class ChoreListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family)
class ChoreListUserView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        user_profile = self.kwargs['user_profile']
        family = UserProfile.objects.get(pk= user_profile).family.id
        return Chore.objects.filter(family=family,participants__in=user_profile)

class ChoreAvailableListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family, participants=None)

class ChoreUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Chore.objects.all()
    serializer_class = ChoreUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)