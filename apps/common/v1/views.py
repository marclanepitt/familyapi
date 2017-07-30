from rest_framework import generics
from common.models import Institution,Major
from . serializers import InstitutionSerializer,MajorSerializer


class InstitutionListView(generics.ListAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class MajorListView(generics.ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
