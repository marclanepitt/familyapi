from ..models import Charge
from rest_framework import generics
from .serializers import ChargeSerializer


class ChargeListCreateView(generics.ListCreateAPIView):
    serializer_class = ChargeSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Charge.objects.filter(family=family)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)