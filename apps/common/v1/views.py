from rest_framework import generics
from .serializers import PetSerializer,FamilySerializer,PostSerializer
from django.shortcuts import get_object_or_404
from common.models import Family,Post


class PetCreateView(generics.CreateAPIView):
    serializer_class = PetSerializer

class FamilyListView(generics.ListAPIView):
    serializer_class = FamilySerializer

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['family'])

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(family=self.kwargs['family']).order_by('-date')