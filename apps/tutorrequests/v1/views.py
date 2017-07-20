from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tutory_api.permissions import IsSelf

from .serializers import TutorRequestSerializer,TutorRequestUpdateSerializer
from tutorrequests.models import TutorRequest


class TutorRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = TutorRequest.objects.all()
    serializer_class = TutorRequestSerializer


class TutorRequestRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = TutorRequest.objects.all()
    serializer_class = TutorRequestSerializer



class TutorRequestUpdate(generics.UpdateAPIView, UpdateModelMixin):
	queryset = TutorRequest.objects.all()
	fields = ['building','location','help_description','subject','type_help', 'amount']
	serializer_class = TutorRequestUpdateSerializer

	def put(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)
