from ..models import Charge
from rest_framework import generics
from .serializers import ChargeSerializer,ChargeCreateSerializer


class ChargeListView(generics.ListAPIView):
    serializer_class = ChargeSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Charge.objects.filter(family=family)

class ChargeCreateView(generics.CreateAPIView):
    serializer_class = ChargeCreateSerializer
    def get_serializer_context(self):
        return {'family': self.kwargs['family']}
