from rest_framework import generics
from .serializers import PetSerializer


class PetCreateView(generics.CreateAPIView):
    serializer_class = PetSerializer