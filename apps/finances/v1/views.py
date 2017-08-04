from ..models import Charge
from rest_framework import generics
from .serializers import ChargeSerializer


class ChargeListView(generics.ListAPIView):
    serializer_class = ChargeSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Charge.objects.filter(family=family)

class ChargeCreateView(generics.CreateAPIView):
    serializer_class = ChargeSerializer