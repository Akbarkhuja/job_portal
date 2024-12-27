from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwards = {
            'password': {'write_only': True}
        }


class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Applicant
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of applicant
        :return: returns a successfully created applicant record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_applicant = True
        user.save()
        
        applicant, created = Applicant.objects.update_or_create(user=user)
        return applicant


class RecruiterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Recruiter
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_recruiter = True
        user.save()

        applicant, created = Recruiter.objects.update_or_create(user=user)
        return applicant
