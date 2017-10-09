from rest_framework import generics
from .serializers import PetSerializer,FamilySerializer,PostSerializer, PetCreateSerializer
from django.shortcuts import get_object_or_404
from common.models import Family,Post, Pet


class PetCreateView(generics.CreateAPIView):
    serializer_class = PetCreateSerializer
    def get_serializer_context(self):
        return {'family': self.kwargs['family']}

class PetListView(generics.ListAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        return Pet.objects.filter(family=self.kwargs['family'])

class FamilyListView(generics.ListAPIView):
    serializer_class = FamilySerializer

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['family'])

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(family=self.kwargs['family']).order_by('-date')