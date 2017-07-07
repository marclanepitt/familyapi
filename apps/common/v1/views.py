from rest_framework import generics
from common.models import Institution
from . serializers import InstitutionSerializer


class InstitutionListView(generics.ListAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
