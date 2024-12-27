from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, 
    IsAdminUser, 
    IsAuthenticated,
    AllowAny
)

from .models import *
from .permissions import *
from .serializers import *

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView


# EDUCATION

class EducationAPIList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EducationAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsApplicant, )
    # authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EducationAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EducatioAPICreate(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# JOB

class JobAPIList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class JobAPICreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsApplicant, )


class JobAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class JobAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# APPLICANTION

class ApplicantionAPIList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ApplicantionAPICreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = (IsApplicant, )


class ApplicantionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ApplicantionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsApplicant, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# VACANCY

class VacancyAPIList(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsRecruiter, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class VacancyAPICreate(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsRecruiter, )


class VacancyAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsRecruiter, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class VacancyAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsRecruiter, )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)