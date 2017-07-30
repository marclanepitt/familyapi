from rest_framework import serializers
from common.models import Institution,Major


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id','institution_id','name','zip_code','website','campus_name','campus_zip')


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('id', 'major', 'category')
