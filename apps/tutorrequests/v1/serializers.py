from django.contrib.auth.models import User
from rest_framework import serializers
from tutorrequests.models import TutorRequest

class TutorRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = TutorRequest
		fields =  ('student', 'tutor', 'id', 'building','location','help_description','subject','type_help', 'amount')


class TutorRequestUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = TutorRequest
		fields =  ('building','location','help_description','subject','type_help', 'amount')
