from rest_framework import serializers

from .models import *
from users.serializers import *


class EducationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Education
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Job
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    position = serializers.RelatedField(source='position', read_only=True)


    class Meta:
        model = Application
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    position = serializers.RelatedField(source='position', read_only=True)
    organization = serializers.RelatedField(source='organization', read_only=True)

    applied = ApplicantSerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'